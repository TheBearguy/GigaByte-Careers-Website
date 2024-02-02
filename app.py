from flask import Flask, render_template,jsonify
from database import load_jobs_from_db, load_job_from_db


app = Flask(__name__)





@app.route("/")
def hello_gigabyte():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs, 
                           company_name = "GigaByte")


@app.route("/api/jobs")
def list_jobs():
    job = load_jobs_from_db()
    return jsonify(job)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job = job)





if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)