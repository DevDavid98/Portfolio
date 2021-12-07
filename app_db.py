from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Projects(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    date_added = db.Column('Dated Added', db.DateTime,
                           default=datetime.datetime.now)

    title = db.Column('Project Name', db.String())

    completed = db.Column('Completion Date', db.String())

    description = db.Column('Decription', db.Text())

    skills = db.Column('Skills', db.Text())

    link = db.Column('Project Link', db.Text())
