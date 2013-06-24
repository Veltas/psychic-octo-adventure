#!/usr/bin/env python

from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from config import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///%s" % DB
db = SQLAlchemy(app)

user_game = db.Table('UserGame',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True)
    steam_name = db.Column(db.String(80), unique=True)
    games = db.relationship('Game', secondary=user_game)

    def __init__(self, name, steam_name):
        self.name = name
        self.steam_name = steam_name

    def __repr__(self):
        return '<User %r>' % self.username

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True)
    free = db.Column(db.Boolean, unique=True)

    def __init__(self, name, free=False):
        self.name = name
        self.free = free

    def __repr__(self):
        return '<Game %r>' % self.name

@app.route('/game', methods=['GET'])
def get_all_games():
    return jsonify(User.query.all())

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(port=PORT, debug=True, host='0.0.0.0')
