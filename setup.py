from setuptools import setup

APP_NAME = "vrs"
APP = ['agent.py']
DATA_FILES = ['trap4scammers.py']

OPTIONS = { 
    'includes': ('os', 'PIL', 'email_to'),
    'iconfile':'image.jpeg'
 }

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)