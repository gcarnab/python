import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, Item

# Set the path to the database file inside the DATA directory
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DATA')
DATABASE_FILE = os.path.join(DATA_DIR, 'items.db')  # Replace with your desired file name
ITEMS_PER_PAGE = 3
IN_MEMORY_DB = False

# Ensure the DATA directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if IN_MEMORY_DB :
    db_uri = 'sqlite:///:memory:'
else :
    # Configure the database URI to use the file-based database
    db_uri = 'sqlite:///' + DATABASE_FILE

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True  # Enable this line to see SQL queries in the console

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Get the current page from the query parameters, default to 1
    page = request.args.get('page', 1, type=int)

    # Paginate the items
    items_pagination = Item.query.paginate(page=page, per_page=ITEMS_PER_PAGE)

    return render_template('index.html', items_pagination=items_pagination)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        item = Item(name=name, description=description)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_item.html')

@app.route('/edit/<int:item_id>')
def edit_item(item_id):
    item = Item.query.get(item_id)
    return render_template('update_item.html', item=item)

@app.route('/update/<int:item_id>', methods=['POST'])
def update_item(item_id):
    item = Item.query.get(item_id)
    item.name = request.form['name']
    item.description = request.form['description']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
