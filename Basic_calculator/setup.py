from setuptools import setup,find_packages

setup(
name='Basic_calculator',
version='0.0.1',
description='A very basic calculator',
Long_description='A very',
url='',
author='palani',
author_email='palaniappan.mca@gmail.com',
License='MIT',
keywords='calculator',
packages=find_packages(),
entry_points={
        'console_scripts': [
                'hello-world-cli = hello_world.main:main',
        ],
},
install_requires=[''],
)
