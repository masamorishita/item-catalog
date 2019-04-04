from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///itemwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#Show all categories and items
@app.route('/')
@app.route('/catalog')
def item():
    category = session.query(Category).order_by(asc(Category.name))
    items = session.query(Item).order_by(asc(Item.id))
    return render_template('item.html', category=category, items=items)

#Show all items in each category
@app.route('/catalog/<category_name>/item/')
def itemWithCategory(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category=category)
    return render_template('item_by_category.html', category=category, items=items)

#Create a new item
@app.route('/catalog/<int:category_id>/item/new/', methods=['GET', 'POST'])
def newItem(category_id):
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form['description'],category_id=category_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('item'))
    else:
        return render_template('newitem.html', category_id=category_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000, threaded = False)