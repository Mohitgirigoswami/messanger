from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'user_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    
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
    timestamp = db.Column(db.DateTime, nullable=False)N