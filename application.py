from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import session as login_session
import random, string
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///itemwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create a state token to prevent request forgery.
# Store it in the session for later validation.
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    #RENDER THE LOGIN TEMPLATE
    return render_template('login.html')


# Show all categories and items.
@app.route('/')
@app.route('/catalog')
def item():
    category = session.query(Category).order_by(asc(Category.name))
    items = session.query(Item).order_by(asc(Item.id))
    return render_template('item.html', category=category, items=items)

# Show all items in each category.
@app.route('/catalog/<category_name>/items')
def itemWithCategory(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category=category)
    return render_template('item_by_category.html', category=category, items=items)

# Show item's description.
@app.route('/catalog/<category_name>/<item_name>')
def itemInformation(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category=category, name=item_name).one()
    return render_template('item_information.html', category=category, items=items)

# Create a new item.
@app.route('/catalog/item/new', methods=['GET', 'POST'])
def newItem():
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form['description'],category_id=request.form['category'])
        session.add(newItem)
        session.commit()

        return redirect(url_for('item'))
    else:
        return render_template('newitem.html')


# Edit an item.
@app.route('/catalog/<item_name>/edit', methods=['GET', 'POST'])
def editItem(item_name):
    editedItem = session.query(Item).filter_by(name=item_name).one()
    categories = session.query(Category)
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['category']:
            editedItem.category_id = request.form['category']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('item'))
    else:
        return render_template('edititem.html', item=editedItem, categories=categories)


# Delete an item.
@app.route('/catalog/<item_name>/delete', methods=['GET', 'POST'])
def deleteItem(item_name):
    deletedItem = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('item'))
    else:
        return render_template('deleteitem.html', item=deletedItem)


# Making an API Endpoint (GET Request).
@app.route('/catalog.json')
def itemJson():
    items = session.query(Item).order_by(Item.id.asc())
    return jsonify(Item=[i.serialize for i in items])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000, threaded = False)