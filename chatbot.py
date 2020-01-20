from flask import Flask,render_template,request,session,jsonify
from login_validation import validate_db  
from addUser import add_user
from bot_response import botResponse,chat_history

darwinBot=Flask(__name__)

darwinBot.secret_key="abc"

@darwinBot.route("/")
def index():
    return render_template("login.html")

@darwinBot.route("/signup")
def index1():
    return render_template("signup.html")

@darwinBot.route("/chatbot")
def darwinChat():
    return render_template("chatbot.html") 
 
@darwinBot.route("/validation", methods = ["GET","POST"] )
def check_credentials():
    data = request.json
    result = validate_db(data["username"], data["password"])
    if (result == "valid"):
        session["username"] = data["username"]
    return result

@darwinBot.route("/NewUser", methods = ["GET","POST"] )
def add_credentials():
    data = request.json
    result = add_user(data)
    return result

@darwinBot.route("/get_uname", methods = ["GET","POST"] )
def uname():
    if(session["username"] != ""):
        a = chat_history(session["username"])
        r = {"username":session["username"], 'bot':a['bot'], 'user':a['user']}
        return r
    return ""

@darwinBot.route("/bot_response", methods = ["GET","POST"] )
def resp():
    data = request.json
    return botResponse(data["user"], session["username"])



@darwinBot.route("/logout")
def logOut():
    session["username"] = ""
    return render_template("login.html")

if __name__ == '__main__':
    darwinBot.run()    