from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = "Housing-predictor"
VERSION= "0.0.1"
AUTHOR="Harsha"
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    description: This function is going to return list of requirements
    mention in requirements.txt file
    
    return This function is going to return a list which contain name of libraries 
    mentioned in requirements.txt file
    """
    with open("requirements.txt", "r") as requirement_file:
        requirements = requirement_file.readlines()  # Read all lines
        requirements = [req.strip() for req in requirements]  # Strip whitespace/newlines
        if "-e ." in requirements:
            requirements.remove("-e .")  # Remove "-e ." if present
        return requirements
    
    

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    packages= find_packages(),
    install_requires = get_requirements_list()
)
