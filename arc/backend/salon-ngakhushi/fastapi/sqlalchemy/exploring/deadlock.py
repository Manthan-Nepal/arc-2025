import time
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session, sessionmaker
from psycopg2.errors import DeadlockDetected

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

MAX_RETRIES = 3
RETRY_DELAY = 0.5

def run_with_retry(session_factory, operation):
    attempt = 0
    while attempt < MAX_RETRIES:
        session: Session = session_factory()
        try:
            operation(session)
            session.commit()
            return  
        except OperationalError as e:
            session.rollback()
            if isinstance(e.orig, DeadlockDetected):
                attempt += 1
                time.sleep(RETRY_DELAY * attempt)
                continue
            raise  # not a deadlock, re-raise
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    raise RuntimeError("Max retries reached due to repeated deadlocks")


def insert_data(session):
    session.execute(text
        ("INSERT INTO my_table (key, value) VALUES (:key, :value)"),
        {"key": "abc", "value": 123}
    )

run_with_retry(SessionLocal, insert_data)
