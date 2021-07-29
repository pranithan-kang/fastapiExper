import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session

from model.base_class import Base
from model.all_table import (SampleTableA, SampleTableB )
from datetime import date

import os

def initdata(session: Session):
    session.add(SampleTableA(column_int=1234, column_str="testing", column_date=date.today()))
    session.add(SampleTableB(column_int=4321, column_str="testing", column_date=date.today()))

@pytest.fixture
def db_session():
    # engine = create_engine(r"sqlite:///:memory:")
    # engine_path = fr"sqlite:///{os.getcwd()}\temp.db"
    engine_path = "postgresql+psycopg2://test_user:test_password@postgres-db:5432/test_postgres_db"

    engine = create_engine(engine_path)
    Base.metadata.create_all(engine)
    session = Session(engine)
    initdata(session)
    session.commit()
    yield session
    # Base.metadata.drop_all(engine)

def test_p_method(db_session):
    pass

def test_d_method(db_session):
    pass