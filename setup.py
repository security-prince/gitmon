"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['gitmon.py']
DATA_FILES = ['_growl.so', '_growlImage.so']
OPTIONS = {'argv_emulation': False, 'iconfile': 'git.icns', 'use_pythonpath': True}

setup(
    author = "Tomas Varaneckas",
    author_email = "tomas.varaneckas@gmail.com",
    description = "Git repository monitor",
    license = "GPLv3",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
