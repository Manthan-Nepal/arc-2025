import time
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from psycopg2.errors import DeadlockDetected

MAX_RETRIES = 3
RETRY_DELAY = 0.5  # seconds

def run_with_retry(session_factory, operation):
    attempt = 0
    while attempt < MAX_RETRIES:
        session: Session = session_factory()
        try:
            operation(session)
            session.commit()
            return  # success
        except OperationalError as e:
            session.rollback()
            if isinstance(e.orig, DeadlockDetected):
                attempt += 1
                time.sleep(RETRY_DELAY * attempt)  # Exponential backoff
                continue
            raise  # not a deadlock, re-raise
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    raise RuntimeError("Max retries reached due to repeated deadlocks")
