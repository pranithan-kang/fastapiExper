from typing import Optional
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine: Optional[Engine] = None

def get_db():
    Session = scoped_session(sessionmaker(bind=engine, autocommit=True))

    db = Session()
    try:
        yield db
    finally:
        db.close()
    