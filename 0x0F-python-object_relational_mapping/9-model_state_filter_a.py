#!/usr/bin/python3
"""function that shows all State objects that contaain the letter a from the
database"""

import sys
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
    for s in session.query(State).filter(State.name.like('%a%'))\
            .order_by(State.id):
        print("{}: {}".format(s.id, s.name))
    session.close()

