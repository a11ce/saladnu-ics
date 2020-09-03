SHELL := /bin/bash

SaladNU-ICS.app:
	rm -rf lib/
	mkdir -p lib/saladnu_ics
	cp saladnu_ics.py lib/saladnu_ics/saladnu_ics.py
	cp res/__init__.py lib/saladnu_ics/__init__.py
	cp -r $$(python3 -c "import site; print(site.getsitepackages()[0])")/PySimpleGUI lib/PySimpleGUI
	platypus -a SaladNU-ICS -o None -f lib/ -f saladnu_ics.py -R -p /usr/local/bin/python3 gui.py