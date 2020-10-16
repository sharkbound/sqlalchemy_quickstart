from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine('sqlite:///db.sqlite')
Base = declarative_base(bind=engine)
session_maker = sessionmaker(bind=engine)
# noinspection PyTypeChecker
session: Session = scoped_session(session_maker)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=255), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f'<User {self.username}>'


def run_basic_models():
    Base.metadata.create_all()
