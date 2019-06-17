from flask import render_template, url_for, flash, redirect
from flaskblog import app

from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


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

