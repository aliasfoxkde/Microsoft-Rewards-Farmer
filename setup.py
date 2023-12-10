from setuptools import setup, find_packages

setup(
    name='MicrosoftRewardsFarmer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'microsoft_rewards_farmer=microsoft_rewards_farmer:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
