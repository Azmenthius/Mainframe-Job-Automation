## Mainframe Job Automation using REXX & Flask ##
## 📌 Project Overview ##
This project automates mainframe job execution, log retrieval, and monitoring using REXX scripts and JCL. It also includes a Flask-based web dashboard for real-time log visualization and email notifications for job failures.

## 📂 Project Structure ## 

mainframe-job-automation/
│── vscode/               # VS Code workspace settings
│── config/               # Configuration files (if needed)
│── jcl/                  # JCL job definitions
│── output/               # Stores job logs
│── scripts/              # REXX scripts for job automation
│── web_dashboard/        # Flask-based UI for log visualization
│── .DS_Store             # (macOS system file, can be ignored)
│── README.md             # Project documentation
│── LICENSE               # License file

## 🛠 Technologies Used ##

REXX – Automates job execution
JCL – Defines mainframe jobs
Flask (Python) – Web dashboard
HTML, CSS, JavaScript – Frontend UI
SQLite/MySQL – Stores job logs
SMTP (Python smtplib) – Sends email alerts
VS Code & z/OS Emulator – Development environment

## 🚀 How to Run the Project Locally ##

## 1️⃣ Clone the Repository ##

git clone https://github.com/your-username/mainframe-job-automation.git
cd mainframe-job-automation

## 2️⃣ Install Dependencies ##

pip install -r requirements.txt

## 3️⃣ Run REXX Scripts ##

Execute the REXX scripts using Regina REXX:

regina scripts/submit_job.rex
regina scripts/check_job.rex
regina scripts/retrieve_logs.rex

## 4️⃣ Start the Flask Web Dashboard ##

cd web_dashboard
python app.py
🔗 Open: http://127.0.0.1:5000/ in your browser to view logs.

## 5️⃣ Check Job Logs ##

Job logs are stored in:
output/logs.txt

## 6️⃣ Receive Email Alerts ##
If a job fails, an email notification is sent via the send_email.py script.

## 📜 License ##
This project is licensed under the MIT License – see the LICENSE file for details.

## 📬 Contact ##
👤 Ashish Kumar
📧 ashish.career99@gmail.com
