#!/usr/bin/python3
"""Script that prints all City objects from the database"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    lines = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for c, s in lines:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()

