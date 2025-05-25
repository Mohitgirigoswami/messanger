from flask import render_template, session, redirect, url_for,request
from . import main_bp
from app.models import Users,user_friend, db,Message

@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/home',methods=["get",'POST'])
def home():
    islogin = session.get('islogin')
    if islogin is not True:
        return redirect(url_for('auth.login'))
    friend = user_friend.query.filter_by(user_id=session.get('id'))
    friends = []
    for f in friend:
        user = Users.query.filter_by(id=f.friend_id).first()
        if user  :
            friends.append(user)
    return render_template("main/home.html",friends = friends) 

@main_bp.route('/search',methods=["get",'POST'])
def search():
    current_user = Users.query.filter_by(id=session.get('id')).first()
    has_searched = 0
    username_to_search = ""
    islogin = session.get('islogin')
    if islogin is not True:
        return redirect(url_for('auth.login'))
    if request.method=="POST":
        has_searched = True
        to_search = request.form.get("username_to_search")
        search_results = Users.query.filter(
            Users.username.like(f"{to_search}%"),
            Users.id != session.get('id')
        ).all()
        # Create a list of user IDs that are already friends with the current user
        existing_friends = user_friend.query.filter_by(user_id=session.get('id')).all()
        frnd_id = [f.friend_id for f in existing_friends]
        return render_template('main/search.html',has_searched=has_searched,current_user=current_user,username_to_search=to_search,search_results=search_results,frnd_id= frnd_id)
    return render_template('main/search.html',has_searched=has_searched,current_user=current_user)

@main_bp.route('/message/<username>',methods=["get",'POST'])
def message(username):
    islogin = session.get('islogin')
    
    if not islogin:
        return redirect(url_for('auth.login'))
    current_user = Users.query.filter_by(id=session.get('id')).first()
    recipient = Users.query.filter_by(username=username).first()
    
    messages = Message.query.filter(
        ((Message.sender_id == current_user.id) & (Message.recipient_id == recipient.id)) |
        ((Message.sender_id == recipient.id) & (Message.recipient_id == current_user.id))
    ).order_by(Message.timestamp.asc()).all()
    
    return render_template('main/message.html', recipient=recipient,messages = messages)