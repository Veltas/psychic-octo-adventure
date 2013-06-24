run:
	./psychic.py

ready:
	sudo apt-get install python-sqlalchemy python-flask
	cp -n config.py.template config.py
