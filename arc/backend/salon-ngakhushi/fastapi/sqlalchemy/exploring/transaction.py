from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import engine
from sqlalchemy.exc import IntegrityError

session = Session()

try:
    user = User(name="Alice", email="alice@example.com")
    session.add(user)
    session.commit()
except IntegrityError:
    session.rollback()  
    print("User could not be added due to database error.")


autocommit_engine = engine.execution_options(isolation_level="AUTOCOMMIT")

transactional_session = sessionmaker(engine)
autocommit_session = sessionmaker(autocommit_engine)

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from unittest import TestCase

# global application scope.  create Session class, engine
Session = sessionmaker()

engine = create_engine("postgresql+psycopg2://...")


class SomeTest(TestCase):
    def setUp(self):
        # connect to the database
        self.connection = engine.connect()

        # begin a non-ORM transaction
        self.trans = self.connection.begin()

        # bind an individual Session to the connection, selecting
        # "create_savepoint" join_transaction_mode
        self.session = Session(
            bind=self.connection, join_transaction_mode="create_savepoint"
        )

    def test_something(self):
        # use the session in tests.

        self.session.add(Foo())
        self.session.commit()

    def test_something_with_rollbacks(self):
        self.session.add(Bar())
        self.session.flush()
        self.session.rollback()

        self.session.add(Foo())
        self.session.commit()

    def tearDown(self):
        self.session.close()

        # rollback - everything that happened with the
        # Session above (including calls to commit())
        # is rolled back.
        self.trans.rollback()

        # return connection to the Engine
        self.connection.close()