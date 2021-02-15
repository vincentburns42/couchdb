# couchdb

Notes on playing with couchdb on a raspberry pi with docker.

# Installation

SSH into Rapsberry Pi, change password and update:

	pi@raspberrypi:~ $ passwd 
	pi@raspberrypi:~ $ sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y && sudo reboot now

Update the hostname:

	pi@raspberrypi:~ $ sudo vi /etc/hostname
	pi@raspberrypi:~ $ sudo cat /etc/hostname 
	couchdb-home-one
	pi@raspberrypi:~ $ sudo reboot

Create a user, add to sudoers and limit ssh:

	pi@couchdb-home-one:~ $ sudo adduser vinny
	pi@couchdb-home-one:~ $ visudo 
	pi@couchdb-home-one:~ $ sudo visudo 
	pi@couchdb-home-one:~ $ sudo grep -A 1 -B 1 vinny /etc/sudoers
	root	ALL=(ALL:ALL) ALL
	vinny    ALL=(ALL:ALL) ALL
	pi@couchdb-home-one:~ $ sudo vi /etc/ssh/sshd_config 
	pi@couchdb-home-one:~ $ grep AllowUsers /etc/ssh/sshd_config 
	AllowUsers vinny

Install docker:

	vinny@couchdb-home-one:~ $ sudo sh get-docker.sh
	vinny@couchdb-home-one:~ $ sudo usermod -aG docker vinny

Create couchdb container:

	vinny@couchdb-home-one:~ $ docker run -p 5984:5984 -d -e \
	COUCHDB_USER=admin -e COUCHDB_PASSWORD=password treehouses/couchdb:2.3.0

# Example Usage

Install python3 and the couchdb package:

	vinny@laptop:~ $ python3 -m virtualenv venv
	vinny@laptop:~ $ source venv/bin/activate
	vinny@laptop:~ $ ip install couchdb
	vinny@laptop:~ $ vim main.py 

		import couchdb

		# Connect to DB and create DB
		couch = couchdb.Server('http://admin:password@couchdb-home-one:5984/')
		db = couch.create('test')

		# Write doc to DB
		doc = {'name': 'vinny'}
		print("Writing to DB: ", doc)
		response = db.save(doc)

		# Read doc from DB
		doc_id = response[0]
		doc = db[doc_id]
		print("Reading from DB: ", doc)

		# Delete DB
		couch.delete('test')

	vinny@laptop:~ $ python main.py 
	Writing to DB:  {'name': 'vinny'}
	Reading from DB:  <Document '57933b7338a4c730ce0dc9cdc4004d62'@'1-155584ecfe1233194543a97695b04b19' {'name': 'vinny'}>
