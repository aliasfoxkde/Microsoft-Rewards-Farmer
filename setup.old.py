from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='MicrosoftRewardsFarmer',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'MicrosoftRewardsFarmer=src.main:main',
        ],
    },
    package_data={'src': ['*']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
