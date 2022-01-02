from setuptools import setup, find_packages

setup(
    name='booldum',
    version='1.0.0',
    packages=find_packages(include=['booldum']),
    install_requires=[
        'python-docx'
    ]
)
