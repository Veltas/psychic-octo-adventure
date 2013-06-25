EVENTID ?= 1560
DBNAME ?= temp.db

run:
	./psychic.py

ready:
	sudo apt-get install python-sqlalchemy python-flask
	[ -f config.py ] || cp -n config.py.template config.py && \
		sed -i 's/^DB=/&'\''$(DBNAME)'\'/ config.py

create-db:
	python -c 'from psychic import db; db.create_all()'

fetch-users: create-db
	curl http://uwcs.co.uk/events/seating/$(EVENTID)/ | \
		xmllint --xpath '//@title' - 2>/dev/null | \
		sed 's/title=//g' | \
		sed "s/\" \"/'\n'/g" | tr \" \' | \
		sed -n '2,$$p' | sed 's/^/insert into user (name) values (/;s/$$/);/' | \
		sort -u | sqlite3 temp.db

clean:
	find . -name '*.pyc' -delete

destroy: clean
	rm -f temp.db config.py
