"""Sparesnmechs Python package setup."""
from setuptools import setup

name = "sparesnmechs"

setup(
    name=name,
    version="0.0.1",
    description="Sparesnmechs project",
    long_description=open("README.rst").read(),
    url="https://pypi.org/manage/projects/{}/".format(name),
    author="Kenneth Mathenge",
    author_email="mathenge362@gmail.com",
    license="MIT License",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
    ],
    install_requires=[
        "django~=3.1.7",
        "psycopg2~=2.8.4",
        "django-environ~=0.4.5",
        "pytest-django~=3.7.0",
        "pytest-cov~=2.8.1",
        "tox~=3.14.1",
        "model-bakery~=1.0.2",
        "flake8~=3.7.9",
        "wheel~=0.34.2",
        "twine~=3.1.1",
        "flake8-docstrings~=1.5.0",
        "graphene-django~=2.15.0",
    ],
    scripts=["bin/snm_manage"],
    include_package_data=True,
)
