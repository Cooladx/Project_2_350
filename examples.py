# CONNECTING TO A COUCHDB SERVER

import couchdb

# Connect to CouchDB server
couch = couchdb.Server('http://127.0.0.1:5984/')

# Create or connect to a database
db = couch.create('example_db')  # This will create a new database
# db = couch['example_db']  # This will connect to an existing database

print("Database created or connected successfully.")


# INSERTING A DOCUMENT

doc = {
    'type': 'person',
    'name': 'John Doe',
    'age': 30,
    'occupation': 'Software Developer'
}

# Insert the document into the database
db.save(doc)
print("Document inserted successfully.")


# RETRIEVING A DOCUMENT

# Retrieve a document by ID
doc_id = 'some_doc_id'
doc = db[doc_id]
print(f"Retrieved document: {doc}")


# UPDATING A DOCUMENT

# Retrieve the document
doc = db[doc_id]

# Update the document
doc['age'] = 31
db.save(doc)
print("Document updated successfully.")


# DELETING A DOCUMENT

# Retrieve the document
doc = db[doc_id]

# Delete the document
db.delete(doc)
print("Document deleted successfully.")


# QUERYING DOCUMENTS

# Define a simple map function
map_fun = '''function(doc) {
  if (doc.type == 'person') {
    emit(doc.name, doc);
  }
}'''

# Query the database
results = db.query(map_fun)
for row in results:
    print(f"Name: {row.key}, Document: {row.value}")