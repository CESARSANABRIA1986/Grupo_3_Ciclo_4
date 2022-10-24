import pymongo
import  certifi

ca =   certifi.where()

client = pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0.jfa5hsc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
baseDatos=client["bd-registro-elecciones"]
print(baseDatos.list_collection_names())