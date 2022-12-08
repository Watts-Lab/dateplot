from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="dateplot",
    version='0.0.1',
    author="Coën D. Needell",
    author_email="coeneedell@gmail.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@github.com:Watts-Lab/dateplot.git",
    py_modules=["app", "dateplot"],
    install_requires=[requirements],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'dateplot = dateplot:cli'
        ]
    }
)
