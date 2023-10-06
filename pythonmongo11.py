import pymongo

##connection with server

connection = pymongo.MongoClient("mongodb://localhost:27017/")
print("server connected....sucessfully!!!1\n\n")

##finding databases

print("list of dbs are : ",connection.list_database_names(),"\n\n")
databases = connection.list_database_names()

## use database

db = connection["store"]

##create collection

rices = db["rices"]

##show collections

print(db.list_collection_names(),"\n")

db.drop_collection("rice")

##insert document 


##show document



