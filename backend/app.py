from flask import Flask, request

#database migration : creating the schema 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from models import db

#instance of class
app = Flask(__name__)

#configure / database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thought.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#initialize the router 
migrate = Migrate(app,db)
db.init_app(app)





