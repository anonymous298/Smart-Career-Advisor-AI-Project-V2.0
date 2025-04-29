from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns Requirments from requirements.txt file
    '''

    with open(file_path, 'r') as file:
        data = file.readlines()
        data = [word.replace('\n','') for word in data]
        data = [word for word in data if word != '-e .']

    return data 

setup(
    author='Talha',
    author_email='tackletalha@gmail.com',
    version='0.2',
    name='Smart-Career-Advisor-AI-V2.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)