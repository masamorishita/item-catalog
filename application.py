from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///itemwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def item():
    category = session.query(Category)
    items = session.query(Item)
    return render_template('item.html', category=category, items=items)

@app.route('/categories/<int:category_id>/item')
def itemWithCategory(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id)
    return render_template('item.html', category=category, items=items, category_id=category_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000, threaded = False)