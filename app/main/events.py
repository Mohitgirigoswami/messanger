from flask import session
from flask_socketio import emit, join_room
from app.models import db, user_friend, Message
from datetime import datetime

def register_events(socketio):
    @socketio.on('connect')
    def connect():
        user_id = session.get('id')
        if user_id:
            join_room(f'user_{user_id}')
            emit('connect', {'data': 'Connected!'}, room=f'user_{user_id}')
            print(f"User {user_id} connected and joined room user_{user_id}")
        else:
            print("User connected but no session id found")
    
    @socketio.on("has_read")
    def handle_read(data):
        messages_to_update = Message.query.filter(
                    Message.recipient_id == session.get('id'),
                    Message.sender_id == data.get('friend_id'),
                    Message.read == False # Only update unread messages
                ).all()
        for msg in messages_to_update:
            msg.read = True
        db.session.commit()    
    
    @socketio.on("add_friend")
    def add_friend(data):
        print("h")
        frnd_id = data['friend_id']
        if session.get('id') is None:
            print("bhj")
            return
        frnd = user_friend.query.filter_by(user_id=session.get('id'), friend_id=frnd_id).first()
        if frnd is not None:
            print("ghvdc")
            return
        frnd = user_friend(user_id=session.get('id'), friend_id=frnd_id)
        db.session.add(frnd)
        db.session.commit()
        print("friend added")

    @socketio.on("send_message")
    def send_msg(data):
        sender_id = session.get('id')
        recipient_id = data.get('recipient_id')
        content = data.get('content')

        if not sender_id or not recipient_id or not content:
            return

        msg = Message(sender_id=sender_id, recipient_id=recipient_id, text=content, timestamp=datetime.utcnow())
        db.session.add(msg)
        db.session.commit()
        print("done")

        # Emit the new message to both the sender and recipient
        emit('new_message', {
            'sender_id': sender_id,
            'recipient_id': recipient_id,
            'content': content,
            'timestamp': msg.timestamp.isoformat()  # Convert to ISO format for JSON
        }, room=f'user_{sender_id}')
        emit('new_message', {
            'sender_id': sender_id,
            'recipient_id': recipient_id,
            'content': content,
            'timestamp': msg.timestamp.isoformat()  # Convert to ISO format for JSON
        }, room=f'user_{recipient_id}')