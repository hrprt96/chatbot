import pymongo
from cryptography import encrypted_text,decrypted_text


client = pymongo.MongoClient("mongodb://admin:admin@cluster0-shard-00-00-1stxt.mongodb.net:27017,cluster0-shard-00-01-1stxt.mongodb.net:27017,cluster0-shard-00-02-1stxt.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.login


def validate_db(username,password):
    cipher=encrypted_text(password,username)
    res = db.users.find( {"username":username, "password":cipher} ).count()
    if(res >= 1):
        return "valid"
    else:  
        return "invalid"    