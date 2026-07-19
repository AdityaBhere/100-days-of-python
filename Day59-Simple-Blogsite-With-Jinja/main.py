from flask import Flask, render_template, url_for
import requests

blogs = requests.get(url="url for the json bin").json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", blogs=blogs)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog_page/<int:index>")
def blog_page(index):
    searched_post = None
    for blog in blogs:
        if blog['id'] == index:
            searched_post = blog
    return render_template("post.html", post=searched_post)

if __name__ == "__main__":
    app.run(debug=True)
