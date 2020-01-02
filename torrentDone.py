from win32 import win32gui
import smtplib, ssl

programName = "qBittorrent v4.1.5" # Use full name from Window
finished = False # Handles loop exit

port = 465  # For SSL
context = ssl.create_default_context()

senderEmail = "sender@gmail.com"
password = input("Password for sender email: ")
receiverEmail = "receiver@gmail.com"
message = """\
Subject: Downloads Finished

This message is sent from Python."""

def sendEmail():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(senderEmail, password)
        server.sendmail(senderEmail, receiverEmail, message)

while finished == False:
    if win32gui.FindWindow(None, programName) == False:
        sendEmail()
        finished = True