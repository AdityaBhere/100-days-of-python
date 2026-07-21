import smtplib

from flask import Flask, render_template, request
import requests

my_email = "your email"
password = "your app password"

# USE YOUR OWN npoint LINK! 👇
posts = requests.get(url="https://api.npoint.io/xxxxxxxxxxx").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.get("/contact")
def contact():
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.post("/contact")
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone_no = request.form["phone"]
    message = request.form["message"]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone_no}\nMessage:{message}")
        connection.close()

    return render_template("contact.html", msg_sent=True)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
