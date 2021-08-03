
from datetime import date
from app.model.sample_table_a import SampleTableA
from sqlalchemy.orm.session import Session

def get_records_table_a(db: Session):
    return db.query(SampleTableA).all()

def add_records_table_a(db: Session):
    db.add(SampleTableA(column_str="testing x", column_date=date.today()))
    db.add(SampleTableA(column_str="testing y", column_date=date.today()))
    db.flush()