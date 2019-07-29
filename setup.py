try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='quancom_ieee',
    version='1.0',
    author='Marco Forte',
    author_email='fortemarco.irl@gmail.com',
    maintainer='John Quinn',
    maintainer_email='john.quinn@ucd.ie',
    packages=['quancom_ieee', 'quancom_ieee.examples'],
    license='LICENSE.txt',
    description='Python classes to read and write to IEEE488 devices through Quancom GPIB card',
    long_description=open('README.txt').read(),
)
