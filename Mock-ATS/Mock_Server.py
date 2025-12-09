from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS For All Routes

# Data Files
JOBS_FILE = 'Jobs.json'
CANDIDATES_FILE = 'Candidates.json'
APPLICATIONS_FILE = 'Applications.json'

# Global Data Lists
JOBS = []
CANDIDATES = []
APPLICATIONS = []

def load_data():
    global JOBS, CANDIDATES, APPLICATIONS
    try:
        if os.path.exists(JOBS_FILE):
            with open(JOBS_FILE, 'r') as f:
                JOBS = json.load(f)
        else:
            JOBS = []
            save_jobs()
    except:
        JOBS = []
        save_jobs()

    try:
        if os.path.exists(CANDIDATES_FILE):
            with open(CANDIDATES_FILE, 'r') as f:
                CANDIDATES = json.load(f)
        else:
            CANDIDATES = []
            save_candidates()
    except:
        CANDIDATES = []
        save_candidates()

    try:
        if os.path.exists(APPLICATIONS_FILE):
            with open(APPLICATIONS_FILE, 'r') as f:
                APPLICATIONS = json.load(f)
        else:
            APPLICATIONS = []
            save_applications()
    except:
        APPLICATIONS = []
        save_applications()

def save_jobs():
    with open(JOBS_FILE, 'w') as f:
        json.dump(JOBS, f, indent=2)

def save_candidates():
    with open(CANDIDATES_FILE, 'w') as f:
        json.dump(CANDIDATES, f, indent=2)

def save_applications():
    with open(APPLICATIONS_FILE, 'w') as f:
        json.dump(APPLICATIONS, f, indent=2)

# Load Data On Startup
load_data()

@app.before_request
def check_auth():
    if request.method == 'OPTIONS':
        return  # Allow Preflight Requests
    auth = request.headers.get('Authorization')
    if not auth or not auth.startswith('Bearer '):
        return jsonify({"error": "Unauthorized"}), 401
    token = auth.split(' ')[1]
    if token != 'Dummy_Key_1608':
        return jsonify({"error": "Invalid token"}), 401

@app.route('/offers', methods=['GET'])
def get_offers():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify({"data": JOBS[start:end]})

@app.route('/candidates', methods=['POST'])
def create_candidate():
    data = request.get_json()
    candidate_id = len(CANDIDATES) + 1
    candidate = {
        "id": candidate_id,
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "emails": data.get("emails", []),
        "phones": data.get("phones", []),
        "cv_url": data.get("cv_url"),
    }
    CANDIDATES.append(candidate)
    save_candidates()
    return jsonify(candidate), 201

@app.route('/candidates', methods=['GET'])
def get_candidates():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify({"data": CANDIDATES[start:end]})

@app.route('/applications', methods=['POST'])
def create_application():
    data = request.get_json()
    app_id = len(APPLICATIONS) + 1
    application = {
        "id": app_id,
        "candidate_id": data.get("candidate_id"),
        "job_id": data.get("job_id"),
        "status": "applied",
    }
    APPLICATIONS.append(application)
    save_applications()
    return jsonify(application), 201

@app.route('/applications', methods=['GET'])
def get_applications():
    job_id = request.args.get('job_id')
    apps = APPLICATIONS
    if job_id:
        apps = [app for app in APPLICATIONS if str(app["job_id"]) == str(job_id)]
    # Add candidate info
    for app in apps:
        candidate = next((c for c in CANDIDATES if str(c["id"]) == str(app["candidate_id"])), None)
        if candidate:
            app["candidate"] = {
                "name": f"{candidate['first_name']} {candidate['last_name']}".strip(),
                "email": candidate["emails"][0]["value"] if candidate["emails"] else None,
                "first_name": candidate["first_name"],
                "last_name": candidate["last_name"],
            }
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify({"data": apps[start:end]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)