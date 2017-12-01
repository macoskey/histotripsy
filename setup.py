# Useful functions for common image/data processing methods performed 
# in the Image-Guided Ultrasound Therapy (aka Histotripsy) lab at the
# University of Michigan Department of Biomedical Engineering
#
# setup.py file
#
#
# Curated by Jonathan J. Macoskey
# https://github.com/macoskey
#
# First created: 12.1.17

<<<<<<< HEAD
from setuptools import setup
# from codecs import open
# from os import path

# here = path.abspath(path.dirname(__file__))
=======
from setuptools import setup, find_packages
#~ from codecs import open
#~ import os

#~ here = os.path.abspath(os.path.dirname(__file__))

#~ with open(os.path.join(here, 'README.rst'),encoding='utf-8') as f:
	#~ long_description = f.read()

>>>>>>> 5db71bd11d916876ba90f3e539dec2c6a6d4c1f5

setup(name='histotripsy',
      version='0.1',
      description='Useful Functions for the Image-Guided Ultrasound Therapy Lab',
      url='https://github.com/macoskey/histotripsy',
      author='Jonathan Macoskey',
      author_email='macoskey@umich.edu',
      license='MIT',
      classifiers=['Development Status :: 3 - Alpha'],
      packages=['histotripsy'],
)
