from setuptools import setup

"""    python setup.py py2app    """

APP_NAME = "envoy"
APP = ['agent.py']
DATA_FILES = []
OPTIONS = {
    'includes': 'pip',
    'iconfile':'image.jpeg'
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)