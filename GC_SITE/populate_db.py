from gc_site import app
from database import db
from models import User
from werkzeug.security import generate_password_hash

def populate_admin():
    with app.app_context():
        # Check if the admin user already exists
        admin_user = User.query.filter_by(username='admin').first()
        if admin_user is None:
            # If admin user does not exist, create one
            admin_password = generate_password_hash('admin')  # Replace 'admin_password' with your desired password
            admin = User(username='admin', password=admin_password, role='admin')
            db.session.add(admin)
            db.session.commit()
            print("Admin user added successfully.")
        else:
            print("Admin user already exists.")

if __name__ == '__main__':
    populate_admin()
