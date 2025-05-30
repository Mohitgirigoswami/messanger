from app import create_app, socketio
from app.models import db

app_instance = create_app()
app = app_instance 
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, host='0.0.0.0',debug=True, port=8000)