""" setup.py file """
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Primaze',
    version='0.0.1',
    # packages=['Pricore', 'Primaze'],
    url='https://github.com/TechnocultureResearch/Primaze',
    license='GNU AGGPL 3',
    author='Satyam Tiwary',
    author_email='satyamtiwary@vvbiotech.com',
    description='Primer Designer for Multiplex RPA Reactions of Allele Specific Targets',
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
