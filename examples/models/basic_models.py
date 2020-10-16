# scoped_session is used for thread safety
from sqlalchemy.orm import scoped_session, sessionmaker

# base class for models
from sqlalchemy.ext.declarative import declarative_base

# the engine is what executes the sql statements
from sqlalchemy import create_engine, Column, Integer, String

# connection string for sqlite database
engine = create_engine('sqlite:///db.sqlite')
# base class used for database table models
Base = declarative_base(bind=engine)

# session maker is called to create sessions
session_maker = sessionmaker(bind=engine)
session = scoped_session(session_maker)


# classes inherit Base to become a model
class User(Base):
    # used to define the name of the table this class matches in the database
    __tablename__ = 'users'

    # primary key
    id = Column(Integer, primary_key=True)
    username = Column(String(length=255), nullable=False)


# create all tables(models) if they do not exists in the database
# Base.metadata.create_all() should be called AFTER all models are created
Base.metadata.create_all()
