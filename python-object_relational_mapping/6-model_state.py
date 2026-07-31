#!/usr/bin/python3
"""
Creates the database and the table states using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine
from model_state import Base

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name)
    )
    Base.metadata.create_all(engine)
