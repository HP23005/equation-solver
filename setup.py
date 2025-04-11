from setuptools import setup, find_packages

setup(
    name="equation-solver",
    version="0.1.0",
    description="Librería para resolver ecuaciones lineales y no lineales con métodos numéricos",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="HP23005",
    author_email="hp23005@ues.edu.sv",
    url="https://github.com/HP23005/equation-solver",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18",
        "scipy>=1.4"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=3.7',
)
