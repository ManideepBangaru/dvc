from setuptools import setup

with open("Readme.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.3",
    author="Manideep Bangaru",
    description="A small package for testing dvc with ML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ManideepBangaru/dvc",
    author_email="bmd994@gmail.com",
    packages=["src/"],
    license="GNU",
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "dvc"
        ]
)