import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"  # Use your email provider's SMTP
SMTP_PORT = 587
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
RECEIVER_EMAIL = "receiver-email@gmail.com"

def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("📩 Email sent successfully!")

    except Exception as e:
        print(f"❌ Error sending email: {e}")

# Check logs for errors
def check_logs_for_errors():
    log_file_path = "../output/logs.txt"  # Adjust path if needed
    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as file:
            logs = file.read()
            if "ERROR" in logs or "FAILED" in logs:
                send_email("🚨 Job Failure Alert", "A mainframe job has failed. Check logs for details.")

if __name__ == "__main__":
    check_logs_for_errors()
