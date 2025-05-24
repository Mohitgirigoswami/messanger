from flask import render_template, session, redirect, url_for,request
from . import main_bp
from app.models import Users,user_friend, db

@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/home',methods=["get",'POST'])
def home():
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
        return render_template('main/search.html',has_searched=has_searched,current_user=current_user,username_to_search=to_search,search_results=search_results)
    return render_template('main/search.html',has_searched=has_searched,current_user=current_user)
