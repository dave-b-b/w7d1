from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

 
# sqlite:///:memory: is used to tell the create_engine that it should use something that is in memory and is not persisted anywhere
# The engine is the connection to the database
engine = create_engine('sqlite:///:memory:')

# Session maker is a factory that generates new session instances
# The bind property is used to tell the session, which connect it is supposed to use.
Session = sessionmaker(bind=engine)

# Sessions store the work that needs to be done. The work isn't persisted to the database until the session.commit() method is invoked.
# Session objects are like cursors 
session = Session()

#  Define base model
# This is used to create a base model from which all other classes can inherit. They can inherit methods and features that allow for the easy table creations

Base = declarative_base()

 

#  Define User model
# When you create a class using the an instance of declarative_base(), there is a metadata property that stores information on ALL the classes that inherit from it.

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    name = Column(String)

    email = Column(String)

 

#  Create tables
#  Based on the information that is in the metadata property (which stores all of the information on classes that inhereit from it), it creates all of the tables.

Base.metadata.create_all(engine)


#  Create
# Schema is defined in the class
new_user = User(name='John Doe', email='john@example.com')


session.add(new_user)

session.commit()

 

#  Read

users = session.query(User).all()

for user in users:

    print(user.name, user.email)

 

#  Update

user_to_update = session.query(User).filter_by(name='John Doe').first()

user_to_update.email = 'john.doe@example.com'

session.commit()

 

#  Delete

user_to_delete = session.query(User).filter_by(name='John Doe').first()

session.delete(user_to_delete)

session.commit()