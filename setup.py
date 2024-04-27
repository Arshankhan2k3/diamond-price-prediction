from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            stripped_line = line.strip()
            if stripped_line:  # Sirf non-empty lines ko hi add karein
                if stripped_line[0].isalpha():  # Sirf alphabetic characters se shuru hone wale lines ko hi add karein
                    requirements.append(stripped_line)  # Har line ko add karein
    return requirements

setup(

    name="DiamondPricePrediction",
    version="0.1.1",
    author="Arshan",
    author_email="arshankhan7619@gmail.com",
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)