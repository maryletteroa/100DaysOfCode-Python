from flask import Flask, render_template, request, redirect, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/ new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()

@app.route("/")
def home():
    return render_template("index.html", books=Books.query.all())

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Books(title = request.form["title"], 
            author = request.form["author"], 
            rating = request.form["rating"])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_rating(id):
    book_to_update = Books.query.get(id)
    if request.method == "POST":
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_rating.html", book=book_to_update)

@app.route("/delete")
def delete():
    id = request.args.get("id")
    book_to_delete = Books.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))




if __name__ == "__main__":
    app.run(debug=True)

