from app import create_app, socketio
from app.models import db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True, host='0.0.0.0', port=8000)