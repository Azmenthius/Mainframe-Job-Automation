import sqlite3
import os

# Database path
DB_PATH = "web_dashboard/database.db"

# Delete the old database if it exists
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print("Old database deleted.")

# Create a new database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create job_logs table with correct columns
cursor.execute("""
CREATE TABLE job_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
    job_id TEXT NOT NULL,
    status TEXT NOT NULL,
    details TEXT NOT NULL
)
""")

# Insert a sample log entry
cursor.execute("""
INSERT INTO job_logs (job_id, status, details) 
VALUES ('JOB12345', 'Completed', 'Job ran successfully')
""")

conn.commit()
conn.close()

print("New database created successfully!")
