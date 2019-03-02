from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

app = Flask(__name__)


@app.route('/')
def item():
    return render_template('item.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000, threaded = False)