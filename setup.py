from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Read the requirements from a file and return a list of packages."""
    with open(file_path, 'r') as file:
        requirements = file.readlines()

    clean_reqs = []
    for req in requirements:
        req = req.split('#')[0].strip()   # Remove comments and spaces
        if req and not req.startswith('-e'):  # Ignore '-e .' lines
            clean_reqs.append(req)

    return clean_reqs


'''
.strip() removes:

leading/trailing spaces
tabs
newlines (\n)

So it already covers what .replace('\n', '') was doing.
'''


setup(
    name='Ml_project',
    version='0.1.0',  # I can change it and according all the packages will be updated
    author='Raja Debnath',
    author_email='rajadebnath0619@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'scikit-learn', 'flask'],  # Add your project dependencies here
    install_requires=get_requirements('requirements.txt'),
    description='A machine learning project setup',
)


