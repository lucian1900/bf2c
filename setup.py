from os.path import join, dirname
from setuptools import setup


with open(join(dirname(__file__), 'requirements.txt')) as f:
    requirements = [x.strip() for x in f.readlines()]


setup(
    name='bf2c',
    version='0.1',
    description='Brainfuck to C compiler',
    packages=['bf2c'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bf2c=bf2c:main',
        ]
    },
    install_requires=requirements,
    zip_safe=False,
)
