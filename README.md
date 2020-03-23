## Heimspiel (Backend)

Did you ever win at undercover plant watering or at hanging up laundry in rainbow colors? Turn your daily tasks into quests and have more fun in everyday life!

Try it out: [https://heimspiel.herokuapp.com/](https://heimspiel.herokuapp.com/)

## WirVsVirus Hackathon

This project was built during the WirVsVirus hackathon.

Link to the [project description](https://devpost.com/software/heimspiel) (German only)

Link to the [hackathon](https://wirvsvirushackathon.org/)

## Technologies used to build this project

Frontend technologies:

- Javascript
- Vue
- Bulma CSS Framework

Backend technologies:

- Python
- Django
- Djangorestframework

The frontend code can be found [here](https://github.com/OpenTechSchool-Leipzig/heimspiel)

## Setup

This project is built with Django Version 3.0.4. Please check if you have a Python version >= 3.6 installed.
```console
foo@bar:~$ python --version
Python 3.7.2
```

Clone the repository:
```console
foo@bar:~$ git clone git@github.com:OpenTechSchool-Leipzig/heimspiel-backend.git
```

Setup a virtual environment:
```console
foo@bar:~$ python -m venv heimspiel-env
```

Install all requirements stored in the `setup.py`:
```console
foo@bar:~$ pip install .
```

Run migrations:
```console
foo@bar:~$ cd src/
foo@bar:~$ python manage.py migrate
```

Start the development server
```console
foo@bar:~$ python manage.py runserver
```

Start coding :-)
