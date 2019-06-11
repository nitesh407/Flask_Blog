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