from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'user_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.String(512), nullable=True)
    email = db.Column(db.String(20), nullable=True)
    avatar_id = db.Column(db.Integer,default = 0)
    
class user_friend(db.Model):
    __tablename__ = 'user_friends'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user_data.id'), nullable=False)
    
class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user_data.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user_data.id'), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    read = db.Column(db.Boolean, nullable=False, default=False) # Corrected line
    timestamp = db.Column(db.DateTime, nullable=False)
    
class Avtar_links(db.Model):
    __tablename__ = 'Avtar_links'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.String(100), nullable=True)