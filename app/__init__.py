from flask import Flask
from flask_socketio import SocketIO
from flask_session import Session
from flask_wtf import CSRFProtect
from .models import db # Assuming this is app/models.py
from .auth import auth_bp
from .main import main_bp
import os
from sqlalchemy.pool import NullPool # <--- ADD THIS IMPORT

socketio = SocketIO()  # Create at module level

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_super_secret_fallback_key_for_dev')
    app.config['WTF_CSRF_SECRET_KEY'] = os.environ.get('WTF_CSRF_SECRET_KEY', 'another_super_secret_fallback_key_for_dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///instance/messenger.db'
    app.config["SESSION_TYPE"] = "sqlalchemy"
    app.config["SESSION_SQLALCHEMY"] = db
    app.config["SESSION_SQLALCHEMY_TABLE"] = "sessions"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # === ADD THESE LINES FOR EVENTLET COMPATIBILITY ===
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "poolclass": NullPool,
        "pool_pre_ping": True,
    }
    # ====================================================

    db.init_app(app)

    # Note: Flask-Session takes the 'db' instance, but it also
    # needs to be initialized AFTER db.init_app(app)
    # The current order is fine: db.init_app(app) then Session(app).

    csrf = CSRFProtect(app) # CSRFProtect should be initialized with the app instance
    sess = Session(app) # Initialize Flask-Session here

    # For SocketIO, make sure `async_mode='eventlet'` is explicitly set, and `cors_allowed_origins` for deployment.
    # manage_session=False is typically used if you are handling sessions through Flask-Session
    socketio.init_app(app, async_mode='eventlet', cors_allowed_origins="*")

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    from app.main.events import register_events
    register_events(socketio)

    # Ensure tables are created if running locally or as part of a one-off task on Render
    with app.app_context():
        db.create_all()

    return app