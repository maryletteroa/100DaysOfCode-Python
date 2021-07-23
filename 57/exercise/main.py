from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender = requests.get(url = "https://api.genderize.io", params={"name": name}).json()["gender"]
    age = requests.get(url = "https://api.agify.io", params={"name": name}).json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)