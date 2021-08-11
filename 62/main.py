from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating_choices = ['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️']  
    coffee_rating = SelectField('Coffee Rating', choices=coffee_rating_choices, validators=[DataRequired()])
    wifi_strength_choices = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
    wifi_strength_rating = SelectField('WiFi Strength Rating', choices=wifi_strength_choices, validators=[DataRequired()])
    power_socket_choices = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']
    power_socket_availability = SelectField('Power Socket Availability', choices=power_socket_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        data = [form.cafe.data, form.location.data, form.opening_time.data,
        form.closing_time.data, form.coffee_rating.data, 
        form.wifi_strength_rating.data, form.power_socket_availability.data ]
        with open('cafe-data.csv', 'a') as cafe_data_file:
            cafe_data_file.write('\n'+','.join(data))
            return redirect(url_for('add_cafe'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)
