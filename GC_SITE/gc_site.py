from flask import Flask, render_template, request, redirect, url_for, session
#from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from database import db  
from models import User
from config import SECRET_KEY, DATABASE_URI, DATABASE_PASSWORD

app = Flask(__name__)
# Set the template folder location (assuming root directory)
app.template_folder = 'templates'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

#db = SQLAlchemy(app)

# Initialize the database
db.init_app(app) 

# Create a test user
@app.before_request
def create_admin_user():
    if request.endpoint == 'login' and not User.query.filter_by(username='admin').first():
        password_hash = generate_password_hash('admin')
        test_user = User(username='admin', password=password_hash, role='admin')  # Assign role 'admin'
        db.session.add(test_user)
        db.session.commit()
'''
def create_test_user():
    if not User.query.filter_by(username='user').first():
        password_hash = generate_password_hash('user')
        test_user = User(username='user', password=password_hash, role='user')
        db.session.add(test_user)
        db.session.commit()
'''


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            session['role'] = user.role
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('home'))

@app.route('/member')
def member():
    #if 'username' in session and session['role'] == 'admin':
    if 'username' in session:
        return render_template('member.html', username=session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
app.run(debug=True)    

