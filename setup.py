from setuptools import setup, find_packages

import vipr_client

setup(
    name='vipr-client',
    version=vipr_client.__version__,
    description='',
    author='Dan Fornika',
    author_email='dan.fornika@bccdc.ca',
    url='',
    packages=find_packages(exclude=('tests', 'tests.*')),
    python_requires='>=3.5',
    install_requires=[
        'requests',
    ],
    entry_points = {
        'console_scripts': ['vipr-client=vipr_client.client:main'],
    }
)
