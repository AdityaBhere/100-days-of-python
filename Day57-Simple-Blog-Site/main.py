from flask import Flask, render_template
import requests
from post import Post
response = requests.get(url="https://api.jsonbin.io/v3/qs/6a44c7fff5f4af5e294bea6a")
all_posts = response.json().get("record")

all_posts_list = []
for post in all_posts:
    post_title = post["title"]
    post_subtitle = post["subtitle"]
    post_body = post["body"]
    post_index = post["id"]
    all_posts_list.append(Post(post_title, post_subtitle, post_body, post_index))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts_list)

@app.route("/post/<int:index>")
def post(index):
    searched_post = None
    for post_object in all_posts_list:
        if post_object.index == index:
            searched_post = post_object
    return render_template("post.html", post=searched_post)


if __name__ == "__main__":
    app.run(debug=True)
