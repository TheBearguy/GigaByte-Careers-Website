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


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("Select * From jobs where id = :val"),{'val': id}
            )
        rows = result.all()
        if len(rows)==0:
            return None
        else:
            return rows[0]._asdict()
        

def add_application_to_db(job_id, application):
    with engine.connect() as conn:
        query = text("INSERT INTO applications(job_id, full_name, email, linkedin_url, educational_background, work_experience, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :educational_background, :work_experience, :resume_url)")
        params = {
            "job_id": job_id,
            "full_name": application['full_name'],
            "email": application['email'],
            "linkedin_url": application['linkedin_url'],
            "educational_background": application['educational_background'],
            "work_experience": application['work_experience'],
            "resume_url": application['resume_url']
        }
        conn.execute(query, params)

