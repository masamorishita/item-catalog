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


#Add categories
category1 = Category(user_id=1, name="Soccer")
category2 = Category(user_id=1, name="Basketball")
category3 = Category(user_id=1, name="Baseball")
category4 = Category(user_id=1, name="Frisbee")
category5 = Category(user_id=1, name="Snowboarding")
category6 = Category(user_id=1, name="Rock Climbing")
category7 = Category(user_id=1, name="Foosball")
category8 = Category(user_id=1, name="Skating")
category9 = Category(user_id=1, name="Hockey")

session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)
session.add(category5)
session.add(category6)
session.add(category7)
session.add(category8)
session.add(category9)

session.commit()