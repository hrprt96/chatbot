import pymongo
import random

client = pymongo.MongoClient("mongodb://admin:admin@cluster0-shard-00-00-1stxt.mongodb.net:27017,cluster0-shard-00-01-1stxt.mongodb.net:27017,cluster0-shard-00-02-1stxt.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.login


def botResponse(input, uname):
    res = db.bot_chat.find_one({"user":input})
    if(db.chat_history.find_one( {"username":uname}) == None):
        db.chat_history.insert_one( {"username":uname,"bot":["Hey,"+uname+"!"],"user":[input] } )
    else:
        db.chat_history.update_one( {"username":uname}, {"$push":{"user":input}} )
    if(res == None):
        reply = "I'm confused, try asking something else!!"
        db.chat_history.update_one( {"username":uname}, {"$push":{"bot":reply}} )
        return reply
    indx=random.randrange(0, len(res["response"])) 
    db.chat_history.update_one( {"username":uname}, {"$push":{"bot":res["response"][indx]}} )   
    return res["response"][indx] 

def chat_history(username):
    chat = db.chat_history.find_one( {"username":username} )
    if(chat == None):
        return ""
    return chat    