from flask import session
from flask_socketio import emit
from app.models import db, user_friend

def register_events(socketio):
    @socketio.on('connect')
    def connect():
        emit('connect')
        print("connected")

    @socketio.on("add_friend")
    def add_friend(data):
        print("h")
        frnd_id = data['friend_id']
        if session.get('id') is None:
            print("bhj")
            return
        frnd = user_friend.query.filter_by(user_id=session.get('id'),friend_id = frnd_id).first()
        if frnd is not None:
            print("ghvdc")
            return
        frnd = user_friend(user_id=session.get('id'), friend_id=frnd_id)
        db.session.add(frnd)
        db.session.commit()
        print("friend added")