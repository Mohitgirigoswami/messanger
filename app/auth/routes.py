from flask import render_template, redirect, request, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Users, db
from app.utils import is_valid, is_strong
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password_hash, password):
            error = "Invalid username or password."
        else:
            session['id']=user.id
            session['islogin'] = True
            session['username'] = user.username
            session['first_name'] = user.first_name
            session['last_name'] = user.last_name
            return redirect(url_for('main.index'))
    return render_template('auth/login.html', error=error)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        user = Users.query.filter_by(username=username).first()
        is_strong_password, msg = is_strong(password)
        if user is not None or not is_valid(username) or not is_strong_password:
            error = "Registration failed. Please check your details and try again."
            return render_template('auth/register.html', error=error)
        user = Users(
            username=username,
            password_hash=generate_password_hash(password),
            first_name=first_name,
            last_name=last_name
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', error=error)

@auth_bp.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
