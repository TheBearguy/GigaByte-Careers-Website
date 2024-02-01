from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "New York, USA",
        "salary": "$100,000"
    },
    {
        "id": 2,
        "title": "Software Engineer",
        "location": "Vancouver, Canada",
        
    },
    {
        "id": 3,
        "title": "Data Scientist",
        "location": "San Francisco, USA",
        "salary": "$150,000"
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "Remote",
        "salary": "$120,000"
    }
]


@app.route("/")
def hello_gigabyte():
    return render_template('home.html', jobs = JOBS, company_name = "Google")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)



if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)