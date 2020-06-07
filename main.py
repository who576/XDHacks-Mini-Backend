# import pyrebase

# config = {
#   "apiKey": "AIzaSyCw8B4O1W2QWvJxLiKkYU7jV1gdxiJ7fN4",
#   "authDomain": "team-ambition---xdhacks-covid.firebaseapp.com",
#   "databaseURL": "https://team-ambition---xdhacks-covid.firebaseio.com",
#   "projectId": "team-ambition---xdhacks-covid",
#   "storageBucket": "team-ambition---xdhacks-covid.appspot.com",
#   "messagingSenderId": "871510031672",
#   "appId": "1:871510031672:web:19d87bd70ed2dcce6fd5cd",
#   "measurementId": "G-S0G3TL5TXP"
# }

# firebase = pyrebase.initialize_app(config)
# db = firebase.database()

# firebase database above
# flask below

from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  list = db.Column(db.String(100), nullable=False)
  name = db.Column(db.String(30), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  email = db.Column(db.String(100), nullable=False)
  number = db.Column(db.String(30), nullable=False)
  city = db.Column(db.String(30), nullable=False)
  category = db.Column(db.String(30), nullable=False)
  about = db.Column(db.String(100), nullable=False)

# ----- add test
# db.create_all()
#     return '<h1>Added New User!</h1>'
# test = User(list='random stuff', name='test', age=20, email='test@example.com', number='123456789', city='Vancouver', category='test', about='something about me')
# db.session.add(test)
# db.session.commit()

# ----- add test 2
# @app.route('/<list>/<name>/<age>/<email>/<number>/<city>/<category>/<about>')
# def index(list,name,age,email,number,city,category,about):
#     user = User(list=list,name=name,age=age,email=email,number=number,city=city,category=category,about=about)
#     db.session.add(user)
#     db.session.commit()

# ----- check test
@app.route('/<name>')
def get_user(name):
  user = User.query.filter_by(name=name).first()

  return f'<h1>age: { user.age }</h1><br><h1>email: { user.email }</h1>'

# ----- routes below

@app.route('/')
@app.route('/index.html')
def base_page():
	return render_template('index.html')

@app.route('/Create.html')
def create_page():
	return render_template('Create.html')

@app.route('/About.html')
def about_page():
	return render_template('About.html')

@app.route('/FAQ.html')
def faq_page():
	return render_template('FAQ.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0')