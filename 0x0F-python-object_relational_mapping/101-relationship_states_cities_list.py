#!/usr/bin/python3

"""function that shows all State objects, and corresponding City objects,
contained in the database"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    lines = session.query(State).all()
    for s in lines:
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("\t{}: {}".format(c.id, c.name))
    session.close()

