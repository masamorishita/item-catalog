# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///itemwithusers.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(
    name="Masa Morishita", email="masam@masamorishita.com", picture='')
session.add(User1)
session.commit()


# Item for each category
item1 = Item(
    user_id=1, name="Stick",
    description="A hockey stick is a piece of sport equipment used bythe players in all the forms of hockey.",
    category_id=9)
item2 = Item(
    user_id=1, name="Goggle",
    description="Goggle is very important for snowboarding to protect your eyes.",
    category_id=5)
item3 = Item(
    user_id=1, name="Snowboard",
    description="Board to enjoy snowboarding.",
    category_id=5)
item4 = Item(
    user_id=1, name="Two Shinguards",
    description="A shin guard or shin pad is a piece of equipment worn on the front of a player's shin to protect them from injury.",
    category_id=1)
item5 = Item(
    user_id=1, name="Shinguards",
    description="A shin guard or shin pad is a piece of equipment worn on the front of a player's shin to protect them from injury.",
    category_id=1)
item6 = Item(
    user_id=1, name="Frisbee",
    description="Frisbee is a gliding toy or sporting item that is generally plastic and roughly 8 to 10 inches (20 to 25 cm) in diameter with a pronounced lip.",
    category_id=4)
item7 = Item(
    user_id=1, name="Bat",
    description="A baseball bat is a smooth wooden or metal club used in the sport of baseball to hit the ball after it is thrown by the pitcher.",
    category_id=3)
item8 = Item(
    user_id=1, name="Jersey",
    description="Clothes suitable for playing soccer games.",
    category_id=1)
item9 = Item(
    user_id=1, name="Soccer Cleats",
    description="Shoes suitable for playing soccer games.",
    category_id=1)

session.add(item1)
session.add(item2)
session.add(item3)
session.add(item4)
session.add(item5)
session.add(item6)
session.add(item7)
session.add(item8)
session.add(item9)

session.commit()
