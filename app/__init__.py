from flask import Flask
from flask_socketio import SocketIO
from flask_session import Session
from flask_wtf import CSRFProtect
from .models import db
from .auth import auth_bp
from .main import main_bp
import os
from sqlalchemy.pool import NullPool 

socketio = SocketIO()  

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_super_secret_fallback_key_for_dev')
    app.config['WTF_CSRF_SECRET_KEY'] = os.environ.get('WTF_CSRF_SECRET_KEY', 'another_super_secret_fallback_key_for_dev')
    basedir = os.path.abspath(os.path.dirname(__file__))
    default_db_path = os.path.join(basedir, '..', 'instance', 'messenger.db')
    default_db_uri = f"sqlite:///{default_db_path}"

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', default_db_uri)
    app.config["SESSION_TYPE"] = "sqlalchemy"
    app.config["SESSION_SQLALCHEMY"] = db
    app.config["SESSION_SQLALCHEMY_TABLE"] = "sessions"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "poolclass": NullPool,
        "pool_pre_ping": True,
    }

    db.init_app(app)

    csrf = CSRFProtect(app) 
    sess = Session(app) 

    socketio.init_app(app, async_mode='eventlet', cors_allowed_origins="*")

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    from app.main.events import register_events
    register_events(socketio)

    with app.app_context():
        db.create_all()

    return app