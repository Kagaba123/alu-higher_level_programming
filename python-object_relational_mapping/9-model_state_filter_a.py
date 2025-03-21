#!/usr/bin/python3
""" lists all State objects that contain
the letter a from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    records = session.query(State).filter(State.name.contains('a')).all()
    for record in records:
        print("{}: {}".format(record.__dict__['id'], record.__dict__['name']))

    session.close()