from flask import Flask
app = Flask(__name__) #app variable here is the object of Flask class, __name__ is simply a name of the module used to locate the other templates of stuffs.
#routes are what we type browsers to go to different pages.Called decorators.They are just to add aditional functionalities to the existing function.s

@app.route("/") #Home page 
@app.route("/home")
def home():
    return "<h1>Hello Nitesh</h1>" 

@app.route("/about")
def about():
	return "<h1>About page</h1>"

if __name__ == '__main__' :
	app.run(debug=True) 


