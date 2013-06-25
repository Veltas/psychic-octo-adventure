#!/usr/bin/env python

from flask import Flask, jsonify, request, render_template
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

    def serialise(self):
        return {  "games" : [game.serialise() for game in self.games],
                  "name" : self.name, "steam_name" : self.steam_name }

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True)
    free = db.Column(db.Boolean)

    def __init__(self, name, free=False):
        self.name = name
        self.free = free

    def __repr__(self):
        return '<Game %r>' % self.name

    def serialise(self):
        return { "id" : self.id, "name" : self.name, "free" : self.free }

@app.route('/game', methods=['GET'])
def get_all_games():
    games = Game.query.order_by(Game.name).all()
    return jsonify({ "games" : [game.serialise() for game in games] })

@app.route('/all', methods=['GET'])
def get_all_users_with_games():
    users = User.query.order_by(User.name).all()
    return jsonify({"data" : [user.serialise() for user in users]})

@app.route('/game', methods=['POST'])
def add_new_game():
    new_game = request.form['name']
    if Game.query.filter_by(name=new_game).first() is None:
      game = Game(new_game)
      db.session.add(game)
      db.session.commit()
      return jsonify({ "success" : "Successfully added game" })
    else:
      return jsonify({ "error" : "Game exists already in db" })

@app.route('/', methods=['GET'])
def root_route():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=PORT, debug=True, host='0.0.0.0')
