from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import MetaData
import datetime

metadata = MetaData()
db = SQLAlchemy(metadata= metadata) 

# create the models 
#User class 
class User(db.Model): 
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = True)
    email = db.Column(db.String(128), nullable= True)
    password = db.Column(db. String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default = False)
    
    #relationship with blog
    blogs_id= db.Column(db.Integer, db.ForeignKey('blogs.id'))
    
    blog = db.relationship('Blog',backref='users', lazy = True)
    
#blog class 
class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db. String, nullable =False)
    content = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, default = True)
   
    user_id = db.Column(db.Integer, db. ForeignKey('users.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    
    #relationship
    user = db.relationship("User" ,back_populates="blogs")
    comments = db.relationship('Comment',back_populates='blogs')
    
#Comment class: 
class Comment(db.Model): 
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String, nullable=False)
    date_posted= db.Column(db.DateTime, default = True)
    # 
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'), nullable=False)
    
    # relationship
    user= db.relationship('User', back_populates='comments') 
    blog = db.relationship('Blog', back_populates = 'comments')
    
