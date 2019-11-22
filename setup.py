from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='payment',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)