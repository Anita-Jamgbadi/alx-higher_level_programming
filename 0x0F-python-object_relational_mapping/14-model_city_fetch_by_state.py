#!/usr/bin/python3
"""
Lists all cities from a db using sqlalchemy
"""

from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    Fetches the states from a given db
    """

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    returned = session.query(City, State).join(State)

    for city, state in returned:
        print('{}: ({}) {}'.format(state.name, city.id, state.name))

    session.commit()
    session.close()
