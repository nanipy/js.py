import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="js",
    version="1.0.0",
    author="Jens Reidel",
    author_email="jens.reidel@gmail.com",
    description="A library that extends Python base classes with their JavaScript default methods.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gelbpunkt/js.py",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
