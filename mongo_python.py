import pymongo
conection = pymongo.MongoClient("mongodb://localhost:27017/")
print("server connected....sucessfully!!!1")

var = myclient["site"]

print(conection.list_databasenames())

x = conection.list_database_names()
if "cst" in x:
    print("db found")
else:
    print("db not found")
