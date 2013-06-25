run:
	./psychic.py

ready:
	sudo apt-get install python-sqlalchemy python-flask
	cp -n config.py.template config.py

create-db:
	python -c 'from psychic import db; db.create_all()'

clean:
	find . -name '*.pyc' | xargs rm
