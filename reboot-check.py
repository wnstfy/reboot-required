#!/usr/bin/env python3
import os
import smtplib
import socket
from email.mime.text import MIMEText

# Fetch the hostname
hostname = socket.gethostname()

# Email Settings
sender_email = "your_email@example.com"
receiver_email = "receiver_email@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587  # or 465 for SSL
smtp_user = "your_smtp_user"
smtp_password = "your_smtp_password"

# Function to send email
def send_email(hostname):
    subject = f"Server Reboot Required on {hostname}"
    body = f"A reboot is required on the server ({hostname}) following an automatic security update."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

# Check for reboot required
if os.path.exists("/var/run/reboot-required"):
    send_email(hostname)
