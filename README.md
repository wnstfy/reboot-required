# Reboot Required Notification

## Overview

Simple Python script to check your server if reboot is required after automatic security updates. Add your own SMTP server and you will receive notification.

### Features

- Check if reboot is required.
- Email notifications.

## Getting Started

These instructions will help you get the project up and running on your local machine or server.

### Prerequisites

Before you begin, make sure you have Python 3.x installed. If you don't have it installed, you can follow these instructions to install Python 3:


- **Linux** (Ubuntu/Debian):
  - Open the terminal and run the following commands to update your package list and install Python 3:
    ```bash
    sudo apt update
    sudo apt install python3
    ```
  - You can verify the installation by running: `python3 --version`.


### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/wnstfy/reboot-required.git
```

2. Navigate to the project directory:

```bash
cd reboot-required
```

### Configuration

Before running the script, configure the `EMAIL SETTINGS` dictionary in the `reboot-check.py` script:

```python
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
```

Make sure to set the SMTP settings for email notifications.

### Usage

Run the script using Python:

```bash
python3 reboot-check.py
```

You can also use the `--verbose` flag to display detailed output:

```bash
python3 reboot-check.py --verbose
```

### Running as a Cron Job

To automate the service checking process, you can set up a cron job to run the script at specified intervals. Here's an example of how to do it:

1. Open your crontab configuration for editing:

```
crontab -e
```

2. Add a new line to schedule the script to run at your preferred frequency. For example, to run the script every day at midnight, add the following line:

```
0 0 * * * * /usr/bin/python3 /path/to/reboot-required/reboot-check.py
```

Make sure to replace `/usr/bin/python3` with the path to your Python 3 interpreter, and `/path/to/reboot-required/` with the actual path to the script's directory.

3. Save and exit the text editor. The script will now run automatically according to your cron job schedule.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to open an issue or create a pull request.

## Contact

For questions or feedback, you can contact the author:

- Simon Gajdosik
