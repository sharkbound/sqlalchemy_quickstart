from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine('sqlite:///db.sqlite')
Base = declarative_base(bind=engine)
session_maker = sessionmaker(bind=engine)
session = scoped_session(session_maker)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=255), nullable=False)


Base.metadata.create_all()
