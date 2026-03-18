from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    
    '''
    this function will return the list of requirements
    '''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.tread
    

setup(
    name='AI-Powered Stock Price Prediction',
    version='0.0.1',
    author='Joshua',
    author_email='josh4global@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)