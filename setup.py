"""
    python setup.py py2app
"""

from setuptools import setup

APP_NAME = "ScanIP"
APP = ['trap4cheater.py']
# APP = ['trap4scammers.py'] # when creating an app file, errors fly out in the console, does not want to work
DATA_FILES = []
OPTIONS = {
    'includes': ('PIL', 'smtplib', 'email'),
    # 'includes': ('PIL', 'email_to'), # this "includes" for the non-working version, an issue with a library that stops working when collapsed into an application project
    'iconfile':'image.jpeg'
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
