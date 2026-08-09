from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Null
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIE_DB_API_KEY = "Get your api key from The Movie Database"
MOVIE_DB_API_URL = "https://api.themoviedb.org/3/search/movie"
FIND_MOVIE_API_URL = "https://api.themoviedb.org/3/movie/"
MOVIE_DB_IMG_URL = "https://image.tmdb.org/t/p/original/"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-list.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", data=all_movies)


#edit form
class RateMovieForm(FlaskForm):
    rating = StringField(label='Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your review', validators=[DataRequired()])
    submit = SubmitField(label='Done')

@app.route("/edit", methods=["POST", "GET"])
def edit():
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_selected.rating = float(form.rating.data)
        movie_selected.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie_selected)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

#adding movie form
class AddMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')

@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_API_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get('id')
    response = requests.get(f"{FIND_MOVIE_API_URL}/{movie_api_id}", params={"api_key": MOVIE_DB_API_KEY})
    data = response.json()
    new_movie = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        img_url=f"{MOVIE_DB_IMG_URL}{data['poster_path']}",
        description=data["overview"],
        review="None",
        rating=0,
        ranking="None",
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
