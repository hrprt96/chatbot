import pymongo
from cryptography import encrypted_text

client = pymongo.MongoClient("mongodb://admin:admin@cluster0-shard-00-00-1stxt.mongodb.net:27017,cluster0-shard-00-01-1stxt.mongodb.net:27017,cluster0-shard-00-02-1stxt.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.login

def add_user(data):
    res = db.users.find( { "username":data["username"] } ).count()
    if (res >= 1):
        return "invalid_uname"
    else :
        data["password"] = encrypted_text(data["password"], data["username"])
        res = db.users.insert_one(data)
        if(res != None):
            return "signedup"
