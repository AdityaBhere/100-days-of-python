# 🎬 Movie Ranking Web App

A movie ranking web application built using **Python and Flask** as part of **Day 64 of my 100 Days of Code** journey.

The application allows users to search for movies using the **TMDB API**, select a movie, add their personal rating and review, and maintain a ranked list of their favourite movies.

## ✨ Features

- 🎬 Search for movies using the TMDB API
- 🔎 Select movies from search results
- 🖼️ Automatically fetch movie posters, descriptions, and release years
- ⭐ Rate movies out of 10
- 📝 Add personal reviews
- 📊 Automatically rank movies based on their ratings
- ✏️ Edit movie ratings and reviews
- 🗑️ Delete movies
- 💾 Store movie information using SQLite
- 🌐 Dynamic web pages using Flask and Jinja2

## 🛠️ Built With

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**
- **Flask-WTF & WTForms**
- **Bootstrap 5**
- **Jinja2**
- **Requests**
- **TMDB API**

## ⚙️ How It Works

### 1. Add a Movie

The user enters the name of a movie in the **Add Movie** page.

The application sends the movie title to the TMDB API and retrieves matching movies.

```text
Movie Title
     ↓
TMDB API Search
     ↓
Matching Movies
     ↓
Select a Movie
````

### 2. Fetch Movie Details

After selecting a movie, the application uses the movie's TMDB ID to request its details.

It retrieves information such as:

* Movie title
* Release year
* Description
* Poster

The movie is then added to the SQLite database.

### 3. Rate & Review

After adding a movie, the user is taken to the **Edit** page where they can provide:

* ⭐ A rating out of 10
* 📝 A personal review

The rating and review are then saved to the database.

### 4. Automatic Ranking

When the home page is loaded, movies are sorted according to their ratings.

The application automatically assigns rankings based on their position in the sorted list, allowing the highest-rated movies to appear at the top.

### 5. Manage Movies

Users can also:

* ✏️ Edit their ratings and reviews
* 🗑️ Delete movies from their ranking list

## 📂 Project Structure

```text
day-64-movie-ranking/
│
├── instance/
│   └── movie-list.db
│
├── static/
│
├── templates/
│   ├── add.html
│   ├── base.html
│   ├── edit.html
│   ├── index.html
│   └── select.html
│
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

1. Clone the repository:

```bash
git clone <GITHUB-REPOSITORY-URL>
```

2. Navigate to the project folder:

```bash
cd day-64-movie-ranking
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Add your TMDB API key to `main.py`.

5. Run the application:

```bash
python main.py
```

6. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## 📚 What I Learned

Through this project, I practiced:

* Building web applications with Flask
* Working with Flask routes and Jinja2 templates
* Creating and managing SQLite databases with SQLAlchemy
* Performing CRUD operations
* Handling and validating forms with Flask-WTF
* Making requests to external APIs
* Working with JSON API responses
* Integrating API data into a web application
* Using Bootstrap to create a web interface

## 🎯 100 Days of Code

**Day 64 / 100**

This project is part of my journey through the **100 Days of Code: The Complete Python Pro Bootcamp**.

Next up: **RESTful APIs 🚀**

```
