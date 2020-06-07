from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, DataRequired
from wtforms.widgets import TextArea

class CreateForm(FlaskForm):
	list = TextAreaField('list', validators=[InputRequired()], widget=TextArea())
	name = StringField('name', validators=[InputRequired()])
	age = IntegerField('age', validators=[InputRequired()])
	email = StringField('email', validators=[InputRequired()])
	tel = StringField('number', validators=[InputRequired()])
	city = StringField('city', validators=[InputRequired()])
	category = StringField('category', validators=[InputRequired()])
	about = TextAreaField('about', validators=[InputRequired()], widget=TextArea())
	submit = SubmitField('Post')
