from flask import Flask, jsonify, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os
import psycopg2
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost/postgres'
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'my_secret_key'
db = SQLAlchemy(app)

class Artist(db.Model):
    artist_id = db.Column(db.Integer, unique=True,primary_key = True,autoincrement=True)
    birth_name = db.Column(db.String(80))
    stage_name = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.String(80))
    solo_debut_date = db.Column(db.String(80))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Member(db.Model):
    artist_id = db.Column(db.Integer,db.ForeignKey('artist.artist_id'),primary_key=True)
    group_name = db.Column(db.String(50),primary_key = True)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Position(db.Model):
	position_id = db.Column(db.Integer, unique=True,primary_key = True,autoincrement=True)
	position_name = db.Column(db.String(50))
	artist_id = db.Column(db.Integer,db.ForeignKey('artist.artist_id'))
	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Group(db.Model):
    group_name = db.Column(db.String(50), unique=True,primary_key = True)
    debut_date = db.Column(db.String(80))
    fandom_name = db.Column(db.String(80))
    official_color = db.Column(db.String(80))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Album(db.Model):
    album_id = db.Column(db.Integer, unique=True,primary_key = True,autoincrement=True)
    album_title = db.Column(db.String(80))
    release_date = db.Column(db.String(80))
    sales = db.Column(db.Integer)
    spotify_url = db.Column(db.String)
    group_name = db.Column(db.String(50),db.ForeignKey('group.group_name'))
        
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Song(db.Model):
    song_id = db.Column(db.Integer, unique=True,primary_key = True,autoincrement=True)
    song_title = db.Column(db.String(80))
    album_id = db.Column(db.Integer,db.ForeignKey('album.album_id'))


    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}





@app.route("/")
@cross_origin()
def hello():
    return "Homepage"

@app.route("/add/group",methods=["GET"])
@cross_origin()
def add_group():
	return render_template("add_group.html")


if __name__ == "__main__":
    app.run()