from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
load_dotenv()
engine = create_engine(os.getenv('DB_CONNECTION_STRING'))

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
    return jobs