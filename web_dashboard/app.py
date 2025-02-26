import os
import sqlite3
from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

# Get the absolute path of the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_logs():
    """Fetch job logs from database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, job_id, status, details FROM job_logs ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    conn.close()
    return logs

@app.route("/")
def index():
    logs = get_logs()
    return render_template("index.html", logs=logs)

@app.route("/submit", methods=["POST"])
def submit():
    """Handles job submission from UI"""
    try:
        job_id = request.form.get("job_id", "JOB" + str(datetime.datetime.now().strftime("%H%M%S")))
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "Completed"
        details = f"Job {job_id} executed at {timestamp}"

        # Insert into SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO job_logs (timestamp, job_id, status, details) VALUES (?, ?, ?, ?)",
                       (timestamp, job_id, status, details))
        conn.commit()
        conn.close()

        return redirect("/")
    
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
