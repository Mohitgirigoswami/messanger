from flask import render_template, session, redirect, url_for,request
from . import main_bp
from app.models import Users,user_friend, db

@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/home',methods=["get",'POST'])
def home():
    friend = user_friend.query.filter_by(session.get('id'))
    username_to_search = " "
    islogin = session.get('islogin')
    if islogin is not True:
        return redirect(url_for('auth.login'))
    if request.method=="POST":
        to_search = request.form.get("username_to_search")
        search_results = Users.query.filter_by(username=to_search)
        
        return render_template('main/home.html',username_to_search=to_search,search_results=search_results,friends=friends,current_user=session.get('username'))
    return render_template('main/home.html',current_user=session.get('username'),friends=friends)

@main_bp.route('/home/add_friend')
def add_friend():
    islogin = session.get('islogin')
    if islogin is not True:
        return redirect(url_for('auth.login'))
    return render_template('main/home.html')