from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from random import choice
from distutils.util import strtobool

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        cafe_dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return cafe_dictionary

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = Cafe().query.all()
    random_cafe = choice(cafes)
    return jsonify(cafe = random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def get_all_cafes():
    return jsonify(cafes = [cafe.to_dict() for cafe in Cafe().query.all()])


@app.route("/search/")
def get_cafe_by_location():
    loc = request.args.get("loc")
    cafe = Cafe().query.filter_by(location=loc).first()
    if cafe:
        return jsonify(cafe = cafe.to_dict())
    else:
        return jsonify(error={"Not found": "Sorry, we don't have a cafe at that location."})

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=strtobool(request.form.get("has_sockets")),
        has_toilet=strtobool(request.form.get("has_toilet")),
        has_wifi=strtobool(request.form.get("has_wifi")),
        can_take_calls=strtobool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def path_update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"})

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct API key"}), 403


if __name__ == '__main__':
    app.run(debug=True)
