import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session

from app.model.base_class import Base
from app.model.all_table import (SampleTableA, SampleTableB )
from datetime import date
from test.fixture.db import *

def test_p_method(db_session: Session):
    db_session.add(SampleTableA(column_int=1234, column_str="testing", column_date=date.today()))
    db_session.flush()
    pass

def test_d_method(db_session: Session):
    db_session.add(SampleTableB(column_int=4321, column_str="testing", column_date=date.today()))
    db_session.flush()
    pass
