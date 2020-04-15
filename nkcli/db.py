from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
Engine = None
Session = None


def setup(url):
    global Engine
    global Session
    Engine = create_engine(url)
    Base.metadata.create_all(Engine)
    Session = sessionmaker(Engine)
    return Session

def create_session():
    global Session
    if not Session:
        Session = sessionmaker(Engine)
    return Session()