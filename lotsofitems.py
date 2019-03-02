from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///itemwithusers.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Create dummy user
User1 = User(name="Masa Morishita", email="masam@masamorishita.com", picture='')
session.add(User1)
session.commit()


#Item for snowboarding
category1 = Category(user_id=1, name="Snowboarding")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Snowboard", description="Board to enjoy snowboarding.",
    category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Goggle", description="Goggle is very important for snowboarding to protect your eyes.",
    category=category1)

session.add(item2)
session.commit()


#Item for baseball
category2 = Category(user_id=1, name="Baseball")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Bat", description="A tool to hit a ball.",
    category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Glove", description="A tool to catch a ball.",
    category=category2)

session.add(item2)
session.commit()
