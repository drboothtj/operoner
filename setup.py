from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    description = fh.read()

setup(
    name="operoner",
    version="0.0.1",
    description="quick and dirty operon prediction in Python",
    long_description=description,
    long_description_content_type="text/markdown",
    author="Dr. Thom Booth",
    author_email="thoboo@biosustain.dtu.dk",
    packages=find_packages(),
    install_requires=[
        'Bio'
        ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "operoner=operoner.main:main",
        ],
    },
)

