from sqlalchemy import (
    Column,
    String,
    Integer,
    Date
)

from model.base_class import Base

class SampleTableB(Base):
    __tablename__ = "sample_table_b"

    id = Column(Integer, primary_key=True)
    column_int = Column(Integer)
    column_str = Column(String)
    column_date = Column(Date)