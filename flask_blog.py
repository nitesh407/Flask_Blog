from flask import Flask, render_template, url_for
app = Flask(__name__) #app variable here is the object of Flask class, __name__ is simply a name of the module used to locate the other templates of stuffs.
#routes are what we type browsers to go to different pages.Called decorators.They are just to add aditional functionalities to the existing function.s


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

if __name__ == '__main__' :
	app.run(debug=True) 


