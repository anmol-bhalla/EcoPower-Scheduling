from app import app, db

# Push an application context
with app.app_context():
    # This script will create the tables in the PostgreSQL database
    db.create_all()