# main_script.py
from app import create_app
from app.models import db, Users # Assuming your Users model is in app.models

# --- Configuration ---
# This is the password hash you provided.
# In a real application, each user should have a unique, securely generated hash.
# For dummy data purposes, we'll use this static one.
PASSWORD_HASH = 'scrypt:32768:8:1$iQCOlha8PFJ1eyN5$94d994ec0444f0f49e765682b8dc51b608afd7cc229a6ec0eedd506baca48196b97c73b35d4ff48d1e2cf18f6dbb69933e6dcf070f377da2dda19d4b123dead1'
NUMBER_OF_USERS = 100

def create_dummy_users():
    """
    Generates and saves a specified number of dummy users to the database.
    """
    app = create_app() # Assuming create_app() initializes your Flask app and SQLAlchemy
    with app.app_context():
        users_to_create = []
        print(f"Preparing to create {NUMBER_OF_USERS} dummy users...")

        for i in range(1, NUMBER_OF_USERS + 1):
            username = f'user{i}'
            first_name = f'FirstName{i}'
            last_name = f'LastName{i}'
            
            # Create a new User object
            user = Users(
                username=username,
                password_hash=PASSWORD_HASH, # All users will have the same password hash
                first_name=first_name,
                last_name=last_name
                # Add any other required fields for your Users model here,
                # possibly with default or generated values.
                # email=f'user{i}@example.com' # Example if you have an email field
            )
            users_to_create.append(user)
            
            if i % 20 == 0: # Print progress
                print(f"Prepared {i}/{NUMBER_OF_USERS} users...")

        if not users_to_create:
            print("No users to create.")
            return

        try:
            print(f"\nAttempting to bulk save {len(users_to_create)} users to the database...")
            # Bulk save the user objects to the session
            db.session.bulk_save_objects(users_to_create)
            # Commit the session to save changes to the database
            db.session.commit()
            print(f"{len(users_to_create)} dummy users created successfully!")
        except Exception as e:
            db.session.rollback() # Rollback in case of error
            print(f"An error occurred: {e}")
            print("Failed to create dummy users.")

if __name__ == '__main__':
    # This part assumes you have a way to define your Users model
    # and db instance before this script runs, or that create_app() handles it.
    
    # Placeholder for Users model and db if not defined via app.models
    # This is just for making the script runnable standalone for demonstration
    # if you don't have the full Flask app structure.
    # In your actual project, you'd rely on your app's structure.
    
    # Example:
    # from sqlalchemy import create_engine, Column, Integer, String
    # from sqlalchemy.orm import sessionmaker, declarative_base
    # from flask_sqlalchemy import SQLAlchemy

    # if not hasattr(db, 'session'): # A simple check
    #     print("Running standalone setup for DB and User model (for demonstration)")
    #     Base = declarative_base()
    #     class Users(Base): # type: ignore
    #         __tablename__ = 'users' # Make sure this matches your actual table name
    #         id = Column(Integer, primary_key=True)
    #         username = Column(String(80), unique=True, nullable=False)
    #         password_hash = Column(String(256), nullable=False)
    #         first_name = Column(String(50))
    #         last_name = Column(String(50))
    #         # email = Column(String(120), unique=True) # Example

    #     # Replace with your actual database URI
    #     engine = create_engine('sqlite:///./test_dummy.db') 
    #     Base.metadata.create_all(engine) # Create table if it doesn't exist
        
    #     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
    #     # Mock db object for standalone run
    #     class MockDB:
    #         def __init__(self):
    #             self.session = SessionLocal()
    #     db = MockDB() # type: ignore

    #     # Mock create_app for standalone run
    #     class MockApp:
    #         def app_context(self):
    #             return self # Simple context manager
    #         def __enter__(self):
    #             return self
    #         def __exit__(self, exc_type, exc_val, exc_tb):
    #             pass
    #     def create_app():
    #         return MockApp()
    
    create_dummy_users()
