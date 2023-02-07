import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jaxboard",
    version="0.0.1",
    description="A tensorboard logger for jax",
    long_description=long_description,
    author="Eduardo Pignatelli",
    author_email="edu.pignatelli@gmail.com",
    url="https://github.com/epignatelli/jaxboard",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "tensorboard",
        "tensorflow>=1.15.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires=">=3.7",
)
