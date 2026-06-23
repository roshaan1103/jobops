# app/db/init_db.py

import time

from app.db.database import engine
from app.db.base import Base

def init_db():

    for attempt in range(20):

        try:
            Base.metadata.create_all(bind=engine)

            print("Database initialized")

            return

        except Exception as e:

            print(f"Database not ready: {e}")

            time.sleep(3)

    raise RuntimeError("Database never became available")