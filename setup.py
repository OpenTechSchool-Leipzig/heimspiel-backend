from setuptools import find_packages, setup

setup(
    name="heimspiel-backend",
    version="0.1",
    url="https://github.com/OpenTechSchool-Leipzig/heimspiel-backend",
    author="OpenTechSchool Leipzig",
    author_email="leipzig@opentechschool.org",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "Django>=3.0.4",
        "django-cors-headers>=3.2.1",
        "django-filer>=1.7.0",
        "djangorestframework>=3.11.0",
        "gunicorn==20.0.4",
        "dj-database-url==0.5.0",
        "psycopg2-binary==2.8.5",
        "whitenoise==5.0.1",
    ],
    extras_require={"test": ["black>=19.10b0"],},
)
