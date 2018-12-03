from flask import Flask, jsonify, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os
import psycopg2
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost/postgres'
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'my_secret_key'
db = SQLAlchemy(app)

class Group(db.Model):
    id = db.Column(db.Integer, unique=True,autoincrement=True,primary_key=True)
    groupName = db.Column(db.String(50), unique=True)
    groupType = db.Column(db.String(80))
    company = db.Column(db.String(80))
    debutDate = db.Column(db.String(80))
    fandomName = db.Column(db.String(80))
    fandomColor = db.Column(db.String(80))
    status = db.Column(db.String(80))
    imgURL = db.Column(db.String(500))
    description = db.Column(db.String(500))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Artist(db.Model):
    id = db.Column(db.Integer, unique=True,primary_key = True,autoincrement=True)
    birthName = db.Column(db.String(80))
    stageName = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.String(80))
    nationality = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    groupId = db.Column(db.Integer)
    imgURL = db.Column(db.String(500))

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Member(db.Model):
    artist_id = db.Column(db.Integer,db.ForeignKey('artist.id'),primary_key=True)
    group_name = db.Column(db.String(50),primary_key = True)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Album(db.Model):
    album_id = db.Column(db.Integer, unique=True,primary_key = True,autoincrement=True)
    album_title = db.Column(db.String(80))
    release_date = db.Column(db.String(80))
    sales = db.Column(db.Integer)
    spotify_url = db.Column(db.String)
    group_name = db.Column(db.String(50),db.ForeignKey('group.groupName'))
        
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


@app.route("/artists",methods=["GET"])
@cross_origin()
def list_artists():
    groupID = request.args.get('groupId')
    if groupID == None:
        artists = Artist.query.all()
        list_artists = []
        for artist in artists:
            list_artists.append(artist.as_dict())
        return jsonify(list_artists)
    else:
        artists = Artist.query.filter_by(groupId=groupID).all()
        list_artists = []
        for artist in artists:
            list_artists.append(artist.as_dict())
        return jsonify(list_artists)



@app.route("/groups",methods=["GET"])
@cross_origin()
def list_groups():
    groups = Group.query.all()
    list_groups = []
    for group in groups:
        list_groups.append(group.as_dict())
    return jsonify(list_groups)

@app.route("/groups/<int:groupID>",methods=["DELETE"])
@cross_origin()
def delete_group(groupID):
    group = Group.query.filter_by(id=groupID).first()
    db.session.delete(group)
    db.session.commit()
    return jsonify(success=True,status_code = 200)

@app.route("/artists/<int:artistID>",methods=["DELETE"])
@cross_origin()
def delete_artist(artistID):
    artist = Artist.query.filter_by(id=artistID).first()
    db.session.delete(artist)
    db.session.commit()
    return jsonify(success=True,status_code = 200)

@app.route("/groups/",methods=["POST"])
@cross_origin()
def add_group():
    data = request.get_json()
    groupName = data['groupName']
    groupType = data['groupType']
    company = data['company']
    debutDate = data['debutDate']
    status = data['status']
    fandomName = data['fandomName']
    fandomColor = data['fandomColor']
    imgURL = data['imgURL']
    description = data['description']
    group = Group(groupName=groupName,groupType=groupType,company=company,debutDate=debutDate,status=status,fandomName=fandomName,
        fandomColor=fandomColor,imgURL=imgURL,description=description)
    db.session.add(group)
    db.session.commit()
    return jsonify(success=True,status_code = 200)


@app.route("/artists/",methods=["POST"])
@cross_origin()
def add_artist():
    data = request.get_json()
    stageName = data['stageName']
    birthName = data['birthName']
    birthday = data['birthday']
    gender = data['gender']
    nationality = data['nationality']
    imgURL = data['imgURL']
    groupId = data['groupId']
    artist = Artist(stageName=stageName,birthName=birthName,birthday=birthday,gender=gender,nationality=nationality,imgURL=imgURL,
        groupId=groupId)
    db.session.add(artist)
    db.session.commit()
    return jsonify(success=True,status_code = 200)

@app.route("/artists/<int:artistID>",methods=["GET","PUT"])
@cross_origin()
def list_artist(artistID):
    if request.method == 'PUT':
        data = request.get_json()
        stageName = data['stageName']
        birthName = data['birthName']
        birthday = data['birthday']
        gender = data['gender']
        nationality = data['nationality']
        imgURL = data['imgURL']
        groupId = data['groupId']
        artist = Artist.query.filter_by(id=artistID).first()
        artist.stageName = stageName
        artist.birthName = birthName
        artist.birthday = birthday
        artist.gender = gender
        artist.nationality = nationality
        artist.imgURL = imgURL
        artist.groupId = groupId
        db.session.commit()
    artist = Artist.query.filter_by(id=artistID).first()
    return jsonify(artist.as_dict())

@app.route("/groups/<int:groupID>",methods=["GET","PUT"])
@cross_origin()
def list_group(groupID):
    if request.method == 'PUT':
        data = request.get_json()
        groupName = data['groupName']
        groupType = data['groupType']
        company = data['company']
        debutDate = data['debutDate']
        status = data['status']
        fandomName = data['fandomName']
        fandomColor = data['fandomColor']
        imgURL = data['imgURL']
        description = data['description']
        group = Group.query.filter_by(id=groupID).first()
        group.groupName = groupName
        group.groupType = groupType
        group.company = company
        group.debutDate = debutDate
        group.status = status
        group.fandomName = fandomName
        group.fandomColor = fandomColor
        group.imgURL = imgURL
        group.description = description
        db.session.commit()
    group = Group.query.filter_by(id=groupID).first()
    return jsonify(group.as_dict())


if __name__ == "__main__":
    app.run()