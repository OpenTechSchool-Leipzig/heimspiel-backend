test:
	python setup.py check -m -s
	black --check src/ setup.py
	cd src && python3 manage.py test
