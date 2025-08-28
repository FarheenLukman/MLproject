from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:# returns the list
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj: # open requirements.txt
        requirements = file_obj.readlines() #lines get readed one by one
        requirements = [req.replace("\n","")for req in requirements] #replace \n by blank

        if HYPHEN_E_DOT in requirements: # doesn't read -e .
            requirements.remove(HYPHEN_E_DOT)

    return requirements  

setup(
    name = 'MLproject',
    version ='0.0.1',
    author = 'Farheen',
    author_email = 'farheenlukman44u@gmail.com',
    packages = find_packages(),#
    install_requires = get_requirements('requirements.txt')# requirements we want

)