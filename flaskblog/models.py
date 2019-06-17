from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
# this is a decorator for reloading the user as per the user _id
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

# These models are reresenting the structure of our database, we can now use those to create the database
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)


	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	#we used a lower case u in herem the reason is we are not referencing the actual class, we are actually referencing the collumn name and the table name.
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"

