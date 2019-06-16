- To run the flask file, just go to the directory and write the command - we are setting an enviornment variable here.
	
	export FLASK_APP=filename.py
	flask run

- This will make your file run. But it has a major drawback, everytime you make a change to the source code, you need to stop  the server and rerun the server to see the changes.
- We can get rid of it just by running our aplication in the debug mode.

	export FLASK_DEBUG=1
	flask run

- We can do this without using the enviornment variables using python.
	
		if __name__ == '__main__':
			app.run(debug=True)


- TO import the templates we use render_template() function.
- We are using a variable posts to access the content of this page list(posts) to the template page.

- Now we gonna use template inheritance, because there is alot of simiar code in all the templates( so we created a htmlpage, layout.html)

- We gonna create a block, so the block is a section thaf child section can override.

- In flask we out css and javascript files in a static directory just because all these are static files.

- To include the static files we use a function named url_for(), is a function that will find the exect location of the routes.

- So from now onwards we gonna work on forms and user validations, fo that we gonna use the wtForms extension for all the user validation because all these are so commom.

- write command in the terminal to install, 

	pip install flask-wtf

- And we created another file called forms.py to split up the procrss of forms.

- To import write, 

	from flask_wtf import FlaskForm

- We gonna write some python classes instead of html forms , they further will get converted to the hmtl forms.

- Now when we use the forms we need a secret key, that will protect us from modifying the cookies and cross-side request attacks and things like that.

- We gonna need some random charactors for the key for that we use:-
	import secrects
	secrects.token_hex(16)

- Now we gonna work with sqlAlchamey that is a python database tool, and a ORM(object Relational Mapper). It allow us to use the database in a easy to use way, you can use different databases without changing the python code, suppose we need different databases at different times then we can just pass the database as a different database url to the sqlAlchemy to connect to and we are good to go.

-  pip install sql-alchemy
	
- __repr__(self):
		this methods is, how our object is printed whenever we print it out

- To use current time as a default time when the time is not specified, we use datetime module and datetime class, the function we gonna use is dadtetime.utcnow
	- We have not putted the () here just because we are passing the function as a argument.(we dont want the default time always to be the curret time, what we want is if the current time is not given then the system time will be used)

- Here we gonna have a one to many relationship bw User and Post class, as one user may have many posts but one post can have only one author.

	- backref is similar to adding another column to the Post model, this allows us to do is when we have a post then we can use this author attribute to get the user to get the user who created the post.
	- The lazy argumant just defines when sqlalchemy loads the data from database. True means that sqlalchemy will load the data as necessary in one go.
	- This posts is not a column its just running an additional query in background

- These models are reresenting the structure of our database, we can now use those to create the database, go to your project directory
	
	from filename import db
	
	db.create_all() - this created our database
	
	from flask_blog import User, Post
	
	user_1 = User(username='Nitesh', email='demo@gmail.com', password='password')
	
	db.session.add(user_1)
	
	user_2 =  user_1 = User(username='Nitesh', email='demo@gmail.com', password='password')
	
	user_2 = User(username='Pawan', email='demo1@gmail.com', password='password1')
	
	db.session.add(user_2)...to tell that the changes are made
	
	db.session.commit()....to commit all the changes
	
	User.query.all()...to get all the users.
	
	User.query.first()..to get the first user.

	User.query.filter_by(username='Nitesh').all()
	....to get all the results who have username similar to the Nitesh.

	user = user.query.get(1)
	....to get a user of specific id.

	user.posts...this returns []
	because we dont have any posts for the user yet.do lets add some posts.

	post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
	post_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user.id)
	db.session.add(post_1)
	db.session.add(post_2)
	db.session.commit()

	user.posts

	for post in user.posts:
     print(post.date_posted)

    post = Post.query.first()
    
    Best feature of sqlalchemy
    post.author
	User('Nitesh', 'demo@gmail.com', 'default.jpg')

 
