from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        # TO remove -e . prsent in the end, we use this.
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='End-to-End-MLProject',
version='0.0.1',
author='Sahil',
author_email='sahilkumar2299@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)