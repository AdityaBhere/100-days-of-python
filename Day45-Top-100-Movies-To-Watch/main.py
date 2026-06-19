import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_list = [movie_name.getText() for movie_name in all_movies]
movie_list = movie_list[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(f"{str(movie)}\n")
