from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="MicrosoftRewardsFarmer",
    version="1.0.0",
    description="A simple bot that uses selenium to farm Microsoft Rewards written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/charlesbel/Microsoft-Rewards-Farmer",
    author="A. Random Developer",
    author_email="author@example.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="sample, setuptools, development",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=requirements,
    extras_require={
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
    package_data={
        "": ["main.py", "accounts.json", "version.txt"],
        "src": ["*.py"],  # This includes all .py files in the src directory
    },
    entry_points={
        "console_scripts": [
            "MicrosoftRewardsFarmer=MicrosoftRewardsFarmer:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/charlesbel/Microsoft-Rewards-Farmer/issues",
        "Funding": "https://donate.pypi.org",
        "Say Thanks!": "",
        "Source": "https://github.com/charlesbel/Microsoft-Rewards-Farmer",
    },
)
