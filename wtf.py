from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, DataRequired
from wtforms.widgets import TextArea

class CreateForm(FlaskForm):
	list = TextAreaField('list', validators=[InputRequired(message="invalid")], widget=TextArea())
	name = StringField('name', validators=[InputRequired(message="invalid")])
	age = IntegerField('age', validators=[InputRequired(message="invalid")])
	email = StringField('email', validators=[InputRequired(message="invalid")])
	tel = StringField('number', validators=[InputRequired(message="invalid")])
	city = StringField('city', validators=[InputRequired(message="invalid")])
	category = StringField('category', validators=[InputRequired(message="invalid")])
	about = TextAreaField('about', validators=[InputRequired(message="invalid")], widget=TextArea())
	submit = SubmitField('Post')
