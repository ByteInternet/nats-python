import os
from setuptools import find_packages, setup

setup(
    name='nats-python',
    version='0.8.0-byte-1',
    packages=find_packages(include=['pynats']),
)
