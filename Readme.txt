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