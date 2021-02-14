import couchdb

#Connect to DB and create DB
couch = couchdb.Server('http://admin:password@couchdb-home-one:5984/')
db = couch.create('test')

#Write doc to DB
doc = {'name': 'vinny'}
print("Writing to DB: ", doc)
response = db.save(doc)

#Read doc from DB
doc_id = response[0]
doc = db[doc_id]
print("Reading from DB: ", doc)

# Delete DB
couch.delete('test')
