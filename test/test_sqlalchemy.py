import pytest

from sqlalchemy.orm.session import Session

import app.model as dbm
from datetime import date

def test_p_method(db_session: Session):
    db_session.add(dbm.SampleTableA(column_int=1234, column_str="testing", column_date=date.today()))
    db_session.flush()
    pass

def test_d_method(db_session: Session):
    db_session.add(dbm.SampleTableB(column_int=4321, column_str="testing", column_date=date.today()))
    db_session.flush()
    pass
