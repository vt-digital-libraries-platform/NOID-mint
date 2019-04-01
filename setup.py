import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="noid-mint",
    version="0.0.2",
    author="Yinlin Chen, Tingting Jiang, Lee Hunter, Jim Tuttle",
    author_email="ylchen@vt.edu, virjtt03@vt.edu, whunter@vt.edu, jjt@vt.edu",
    description="Mint NOID",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VTUL/NOID",
    scripts=['bin/noid'],
    packages=setuptools.find_packages(),
    install_requires=[
        'pyyaml'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
