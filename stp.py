"""
    python stp.py py2app
"""

from setuptools import setup

APP_NAME = "envoy"
APP = ['agent.py']
DATA_FILES = []
OPTIONS = {
    'includes': ('PIL', 'smtplib', 'email'),
    'iconfile':'image.jpeg'
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
