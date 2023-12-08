from setuptools import find_packages,setup
from typing import List

##Declaring the variables for setup functions

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT  = "-e ."

def get_requirements()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_lst = requirement_file.readlines()
        requirement_lst = [requirement_name.replace("\n","") for requirement_name in requirement_lst]
        if HYPHEN_E_DOT in requirement_lst:
            requirement_lst.remove(HYPHEN_E_DOT)
        return requirement_lst    

setup(
    name= "sensor",
    version="0.0.1",
    author="ineuron_industry_ready_projects",
    author_email= "jayashreekdsba@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements(),
    )