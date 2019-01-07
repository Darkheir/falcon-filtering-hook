from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development :: Libraries",
]

setup(
    name="falcon_filtering",
    author="Raphael Cohen",
    author_email="raphael.cohen.utt@gmail.com",
    url="https://github.com/darkheir/falcon-filtering-hook",
    version="0.0.1",
    classifiers=classifiers,
    description="Falcon filtering helper",
    long_description=open("README.rst").read(),
    keywords="falcon filtering filter filters api",
    packages=find_packages(include=("falcon_filtering*",)),
    install_requires=["falcon>=0.3"],
    include_package_data=True,
    license="MIT",
)
