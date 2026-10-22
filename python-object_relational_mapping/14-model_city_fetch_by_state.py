#!/usr/bin/python3
"""List all cities with their state names in ascending city ID order."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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
    results = session.query(State, City).join(
        City, State.id == City.state_id
    ).order_by(City.id)
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
