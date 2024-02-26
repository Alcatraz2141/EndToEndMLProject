from setuptools import find_packages,setup
from typing import List

hyp_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Function to read requirements.txt file

    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[line.replace('\n',' ') for line in requirements]

        if hyp_e_dot in requirements:
            requirements.remove(hyp_e_dot)
    return requirements


setup(
    name='EndtoENdMLProject',
    version='0.0.1',
    author='Ruchir',
    author_email='ruchir@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
     )