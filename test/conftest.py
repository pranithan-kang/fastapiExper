""" Fixture to connect to SQLAlchemy """
import os
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.model.base_class import Base

# https://stackoverflow.com/questions/58660378/how-use-pytest-to-unit-test-sqlalchemy-orm-classes

@pytest.fixture(name="db_engine", scope='function')
def fixture_db_engine():
    """creates and yields SQLAlchemy Database Engine"""
    engine = create_engine(os.getenv("CONNECTION_STRING"), echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture(name="db_session_factory", scope='function')
def fixture_db_session_factory(db_engine):
    """returns a SQLAlchemy scoped session factory"""
    return scoped_session(sessionmaker(bind=db_engine, autocommit=True))


@pytest.fixture(name="db_session", scope='function')
def fixture_db_session(db_session_factory):
    """yields a SQLAlchemy connection which is rollbacked after the test"""
    session = db_session_factory()

    yield session

    # session.rollback()
    session.close()
