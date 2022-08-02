from setuptools import setup

APP = ['agent.py']
DATA_FILES = []
OPTIONS = { 
    'iconfile':'image.jpeg',
    'argv_emulation': True,
    'packages': ['os','PIL','smtplib','email.message']
 }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['Pillow'],
)