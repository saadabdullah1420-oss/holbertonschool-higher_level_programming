#!/usr/bin/python3
"""Print the state with the lowest ID, or Nothing if no states exist."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        URL.create(
            "mysql+mysqldb",
            username=sys.argv[1],
            password=sys.argv[2],
            host="localhost",
            port=3306,
            database=sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
