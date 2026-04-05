from setuptools import find_packages, setup
from typing import List
from src.logger import logging

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function returns the list of requirements.'''

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.strip().startswith('#')]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='manoj',
    author_email='manojmanu914822@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)



      