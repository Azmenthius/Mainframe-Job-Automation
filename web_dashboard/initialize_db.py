import sqlite3

DB_FILE = "web_dashboard/database.db"

# Connect to SQLite database (this will create the file if it doesn’t exist)
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create job_logs table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS job_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL,
    status TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("✅ Database initialized successfully!")
