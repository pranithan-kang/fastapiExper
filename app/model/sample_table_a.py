from sqlalchemy import (
    Column,
    String,
    Integer,
    Date
)

from app.model.base_class import Base

class SampleTableA(Base):
    __tablename__ = "sample_table_a"

    id = Column(Integer, primary_key=True)
    column_int = Column(Integer)
    column_str = Column(String)
    column_date = Column(Date)