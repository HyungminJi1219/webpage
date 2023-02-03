from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY goes here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'SQLADDRESS goes here'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

