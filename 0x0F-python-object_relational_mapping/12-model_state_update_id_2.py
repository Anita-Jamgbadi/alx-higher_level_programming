#!/usr/bin/python3
"""
Changes the name of a state in a db using sqlalchemy
"""

from model_state import Base, State
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

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'

    session.commit()
    session.close()
