from flask import render_template, session, redirect, url_for,request
from . import main_bp
from app.models import Users,user_friend, db,Message,Avtar_links
from app.utils import is_valid

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
        if user :
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
        return render_template('main/search.html',has_searched=has_searched,current_user=current_user,username_to_search=to_search,search_results=search_results)
    return render_template('main/search.html',has_searched=has_searched,current_user=current_user)

@main_bp.route('/message/<username>',methods=["get",'POST'])
def message(username):
    islogin = session.get('islogin')
    if not islogin:
        return redirect(url_for('auth.login'))
    current_user = Users.query.filter_by(id=session.get('id')).first()
    recipient = Users.query.filter_by(username=username).first()
    if(current_user.id == recipient.id):
        return redirect(url_for('main.profile', username=current_user.username))
    messages = Message.query.filter(
        ((Message.sender_id == current_user.id) & (Message.recipient_id == recipient.id)) |
        ((Message.sender_id == recipient.id) & (Message.recipient_id == current_user.id))
    ).order_by(Message.timestamp.asc()).all()
    
    return render_template('main/message.html', recipient=recipient,messages = messages)

@main_bp.route('/user/<username>',methods=["get",'POST'])
def profile(username):
    if not session.get('id'):
        return redirect(url_for("main.index"))
    user = Users.query.filter_by(username=username).first()
    is_self = 0 if user.id != session.get('id') else 1
    is_frnd = 1 if not is_self and user_friend.query.filter_by(user_id=session.get('id') ,friend_id = user.id).first() else 0
    return render_template('main/profile.html',user=user,is_self=is_self,is_frnd=is_frnd,avatar_link = (Avtar_links.query.filter_by(id=user.avatar_id).first()).link)

@main_bp.route('/edit_profile',methods=["get",'POST'])
def edit_profile():
    if not session.get('id'):
        return redirect(url_for("main.index"))
    user =  Users.query.filter_by(id =session.get('id')).first()
    if request.method == 'POST':
        error = 0
        new_username = request.form.get('username')
        new_bio = request.form.get('bio')
        new_first_name = request.form.get('first_name')
        new_last_name = request.form.get('last_name')
        if new_username != user.username:
            if not is_valid(new_username):
                error = "Invalid username format. Usernames can only contain alphanumeric characters, underscores, and periods."
            else:
                existing_user = Users.query.filter_by(username=new_username).first()
                if existing_user:
                    error = "This username is already taken. Please choose another."
                else:
                    user.username = new_username
                    session['username'] = new_username # Update session as well
        user.bio = new_bio
        user.first_name = new_first_name
        user.last_name = new_last_name
        
        session['first_name'] = new_first_name
        session['last_name'] = new_last_name

        if error:
            db.session.rollback() # Rollback changes if there's an error
            return render_template('main/edit_profile.html', user=user, error=error)
        else:
            db.session.commit()
            return redirect(url_for('main.profile', username=user.username))
    return render_template('main/edit_profile.html',user = user , error = 0)

@main_bp.route('/change_avtar',methods=["get",'POST'])
def change_avtar():
    if session.get('id') is None:
        return redirect(url_for('auth.login'))
    user = Users.query.filter_by(id=session.get('id')).first()
    if request.method == 'POST':
        new_avatar_id = int(request.form.get('avtar_id'))
        user.avatar_id = new_avatar_id
        db.session.commit()
        return redirect(url_for('main.profile', username=user.username))
    
    all_avatars = Avtar_links.query.order_by(Avtar_links.id).all()
    print(f"Avatars fetched from DB: {all_avatars}")
    return render_template('main/change_avtar.html', avtars=all_avatars, user=user)
