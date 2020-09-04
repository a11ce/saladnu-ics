SHELL := /bin/bash

dist/SaladNU-ICS.zip:
	rm -rf dist/
	rm -rf build/lib/
	mkdir -p dist
	mkdir -p build/lib/saladnu_ics
	cp saladnu_ics.py build/lib/saladnu_ics/saladnu_ics.py
	cp res/__init__.py build/lib/saladnu_ics/__init__.py
	cp -r $$(python3 -c "import site; print(site.getsitepackages()[0])")/PySimpleGUI build/lib/PySimpleGUI
	
	platypus -a SaladNU-ICS -o None -f build/lib/ -f saladnu_ics.py -f gui.py -f /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8 -R -p /bin/sh res/run.sh dist/SaladNU-ICS.app
	cd dist/ && zip -r SaladNU-ICS.zip SaladNU-ICS.app