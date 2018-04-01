#!/usr/bin/env python3
# *_* coding:utf-8 *_*

from flask import Flask
from flask import *
import os
import json 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)

engine = create_engine('mysql://root:@localhost/shiyanlou')
Session = sessionmaker(bind=engine)
session = Session()





class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('files', lazy='dynamic'))
    content = db.Column(db.Text)

    def __init__(self, title, ctime, category, content):
        self.title = title
        self.created_time = ctime
        self.category = category
        self.content = content

    def __repr__(self):
        return '<File %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name






@app.route('/')
def index():
    flist = session.query(File).all()
    return render_template('index.html',flist=flist)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404



@app.route('/files/<file_id>')
def file(file_id):
    onefile = session.query(File).filter(File.id==file_id).first()
    if onefile is None:
        abort(404)
    return render_template('file.html', onefile=onefile)









