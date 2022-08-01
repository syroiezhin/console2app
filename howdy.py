from email_to import Message, EmailServer

def shape():
  try: myhtml = f"""cool"""
  except: myhtml = "ERROR :("
  finally:
    sender = "7kipgod@gmail.com"
    destination = "svaller22@gmail.com"
    
    # create a password for the app bot and get the password by putting it in brackets : https://myaccount.google.com/apppasswords
    EmailServer('smtp.gmail.com', 587, sender, "eifjuipuczaxguxb").send_message(Message(myhtml), destination, "Попался, который кусался!")

if __name__ == "__main__": shape()