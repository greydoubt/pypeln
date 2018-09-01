import os
from setuptools import setup, find_packages

install_requires = [
    
]

setup(
    name = "pypline",
    version = "0.0.1",
    author = "Cristian Garcia",
    author_email = "cgarcia.e88@gmail.com",
    description = (""),
    license = "MIT",
    keywords = [],
    url = "https://github.com/cgarciae/pypline",
   	packages = find_packages(),
    package_data={
        '': ['LICENCE', 'requirements.txt', 'README.md', 'CHANGELOG.md'],
    },
    include_package_data = True,
    install_requires = install_requires,
)