from setuptools import setup

"""    python setup.py py2app    """

APP_NAME = "envoy"
APP = ['agent.py']
DATA_FILES = []
OPTIONS = {
    'includes': ['PIL','smtplib','email'],
    'packages': ['PIL','smtplib','email'],
    'iconfile':'image.jpeg'
}

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