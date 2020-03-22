from setuptools import find_packages, setup

setup(
    name="heimspiel-backend",
    version="0.1",
    packages=find_packages(),

    install_requires=[
        "Django>=3.0.4",
        "django-cors-headers>=3.2.1",
        "django-filer>=1.7.0",
        "djangorestframework>=3.11.0",
    ],

    author="OpenTechSchool Leipzig",
)
