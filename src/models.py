import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, nullable=True)
    user_to_id = Column(Integer, nullable=True)
    user = relationship('User', backref='follower', lazy=True)
    user = relationship('User', backref='follower', lazy=True)

class User(Base):
    __tablename__ = 'user'
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(20), primary_key=True)
    follower_id = Column(Integer,ForeignKey('follower.id'))


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    autor_id = Column(Integer)
    post_id = Column(Integer, nullable=False)
    user = Column(Integer,ForeignKey('user.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    user_id = Column(Integer)
    user = Column(Integer,ForeignKey('user.id'))
    comment = Column(Integer,ForeignKey('comment.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    types = Column(String(250))
    url = Column(String(250))
    post = Column(Integer,ForeignKey('post.id'))






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
