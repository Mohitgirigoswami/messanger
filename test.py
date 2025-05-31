# create_avatars.py
# (Place this file in the root of your Flask project, or a scripts folder)

import os
from app import create_app, db # Adjust 'app' if your __init__.py is elsewhere
from app.models import Avtar_links # Import your model

def insert_github_avatar_links(num_links=35):
    """
    Inserts a series of GitHub raw avatar links into the Avtar_links table.
    This script runs within the Flask application context.
    """
    
    # Define the base URL and pattern for your avatars
    base_url = "https://raw.githubusercontent.com/alohe/avatars/main/png/memo_"
    file_extension = ".png"

    # Create Flask app context
    app = create_app() # Assuming you have a create_app() function
    with app.app_context():
        print("Flask application context entered.")
        try:
            # Generate and insert the links
            for i in range(1, num_links + 1):
                avatar_link = f"{base_url}{i}{file_extension}"
                
                # Check if the link already exists to avoid duplicates
                existing_link = Avtar_links.query.filter_by(link=avatar_link).first()
                if existing_link:
                    print(f"Skipped (already exists): {avatar_link}")
                else:
                    new_avatar = Avtar_links(link=avatar_link)
                    db.session.add(new_avatar)
                    db.session.commit() # Commit each insertion or batch at the end
                    print(f"Inserted: {avatar_link}")
            
            # If you prefer to commit all at once at the end (more efficient for large batches):
            # db.session.commit() 
            # print("All avatar links processed and committed.")

            print("\n--- Verifying inserted links ---")
            all_avatars = Avtar_links.query.order_by(Avtar_links.id).all()
            for avatar in all_avatars:
                print(f"ID: {avatar.id}, Link: {avatar.link}")
            print(f"Total links in table: {len(all_avatars)}")

        except Exception as e:
            db.session.rollback() # Rollback on error
            print(f"An error occurred: {e}")
        finally:
            print("Flask application context exited.")

if __name__ == "__main__":
    insert_github_avatar_links(num_links=35)