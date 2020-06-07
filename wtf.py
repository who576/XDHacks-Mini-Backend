from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

# ('/<list>/<name>/<age>/<email>/<number>/<city>/<category>/<about>')

class CreateForm(FlaskForm):
  list = StringField('list', validators=[InputRequired(message="list required")])
  name = StringField('name', validators=[InputRequired(message="name required")])
  age = IntegerField('age', validators=[InputRequired(message="age required")])
  email = StringField('email', validators=[InputRequired(message="age required")])
  number = StringField('number', validators=[InputRequired(message="number required")])
  city = StringField('city', validators=[InputRequired(message="city required")])
  category = StringField('category', validators=[InputRequired(message="category required")])
  about = StringField('about', validators=[InputRequired(message="about required")])
