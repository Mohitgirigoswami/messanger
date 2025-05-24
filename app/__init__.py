
from flask import Flask
from flask_socketio import SocketIO
from flask_session import Session
from flask_wtf import CSRFProtect
from .models import db
from .auth import auth_bp
from .main import main_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "erjnjrnuergkjerngngjkngkjngnjrngjnjgntrkjg"
    app.config['WTF_CSRF_SECRET_KEY'] = "egtjtrnglerkgnklerngklerngklernlgklrgnl"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config["SESSION_TYPE"] = "sqlalchemy"
    app.config["SESSION_SQLALCHEMY"] = db
    app.config["SESSION_SQLALCHEMY_TABLE"] = "sessions"
    db.init_app(app)
    csrf = CSRFProtect(app)
    Session(app)
    socketio = SocketIO(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    return app, socketio