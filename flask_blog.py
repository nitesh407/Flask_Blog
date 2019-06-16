from flask import Flask, render_template, url_for, flash, redirect
 #app variable here is the object of Flask class, __name__ is simply a name of the module used to locate the other templates of stuffs.
#routes are what we type browsers to go to different pages.Called decorators.They are just to add aditional functionalities to the existing function.s
from flask_sqlalchemy import  SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '49aac1b9a7fa7bb85c7f26e85ef5ff21'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# These models are reresenting the structure of our database, we can now use those to create the database
class User(db.Model):
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



posts = [
	{
		'author':'Nitesh Sharma',
		'title': 'First bolg',
		'content': 'First blog content',
		'date_posted' : 'October 23, 2019'
	},
	{
		'author':'Shiva reddy',
		'title': 'Second blog',
		'content': 'Second blog content',
		'date_posted' : 'October 30, 2019'
	}


]


@app.route("/") #Home page 
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form 	)



@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		if form.email.data == 'snitesh407@gmail.com' and form.password.data == 'nitesh@123':
			flash(f'Welcome {form.email.data}', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'login unsuccessful. Please check username or password', 'danger')
	return render_template('login.html', title='Login', form=form)




if __name__ == '__main__' :
	app.run(debug=True) 


