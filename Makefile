udi-noaa-poly.zip: server.json
	cp README.md ../docs/udi-noaa-poly.md
	zip -r ../udi-noaa-poly.zip LICENSE Makefile POLYGLOT_CONFIG.md \
		README.md noaa.py install.sh nodes profile requirements.txt server.json
