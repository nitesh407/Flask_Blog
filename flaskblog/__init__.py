
from flask import Flask
 #app variable here is the object of Flask class, __name__ is simply a name of the module used to locate the other templates of stuffs.
#routes are what we type browsers to go to different pages.Called decorators.They are just to add aditional functionalities to the existing function.s
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '49aac1b9a7fa7bb85c7f26e85ef5ff21'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes