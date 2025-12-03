from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.0.1",
    author="Claudio Lopez",
    packages=find_packages(),
    install_requires = requirements,
)

#run this command from the root dir to install all dependencies
#pip install -e .