# Importing Flask libraries

from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask import Flask
from flask import session
from flask import jsonify
# Importing time library
import time
# Importing the threading library
from threading import Thread

from client import Client

name="name"
messages = list()
KEY_NAMESS = name
temp=None
user = temp

# creating a flask app
creating_app = Flask(__name__)
print("creating a key for the flask app")
creating_app.secret_key = "key"
#creating a key for the flask app


print("Logout function is calling.....")
@creating_app.route("/logout")
def logout():

    # Whenever a user is logging out we are removing his name from the session[KEY_NAMES]
    print("User trying to logging out....")
    temp2=None
    session.pop(KEY_NAMESS, temp2)
    print("User logged out succesfully....")
    return redirect(url_for("login"))

print("Login function is called......")
@creating_app.route("/login", methods=["POST","GET"])
def login():
    # Here we are adding the name of the user to the session
    print("post request method is functioning.......")
    if request.method == "POST":

        print(f"Here we are adding the name of the user to the session ")
        session[KEY_NAMESS] = request.form["usernameinput"]
        # so we have added the user name
        print("Redirecting to the Home HTML page")
        string_home="home"
        return redirect(url_for(string_home))

    # returning to login.html template
    login_page="login.html"
    return render_template(login_page, **{"session":"session"})




print("Home function is calling..")
@creating_app.route("/")
@creating_app.route("/home")
def home():
    # if the Name of the user is not present in the session, then it will redirect ot to the login url
    print("Name is not in session , redirecting to login url")
    global user
    #checking names in the session...
    if KEY_NAMESS not in session:
        print("returning to login..")
        return redirect(url_for("login"))
    #collecting new user address
    user = Client(session[KEY_NAMESS])
    # returning the index.html template
    index_page="index.html"
    return render_template(index_page, **{"login":True, "session": session})




print("getting_messages function is called....")

@creating_app.route("/getting_messages")
def getting_messages():
    # here we rae getting the messages
    # jsonify functionality from flask
    print("jsonify from flask is in operation")
    messages_1="message_to_print"
    return jsonify({messages_1: messages})

print("sending_messages function is called....")
@creating_app.route("/sending_messages", methods=["GET"])
def sending_messages():

    global user
    # Getiing the message typed by the user on the chatting webpage
    print("message recived from JS sent by the user")
    msg = request.args.get("incoming_message")
    if user:
        user.sharing_message(msg)

    return "none"


print("update_messages function is called....")
def update_messages():
    # we are accesing hte global variable
    cond = True
    global messages

    while cond:
        # setting up some time for sleep
        sleep_time=0.1
        time.sleep(sleep_time)
        # checking for condition that if there is no client then continue the loop
        if not user:
            #skipping the condition if not client
            continue

        print("Fetching the messages from the client---")
        new_messages_from_client = user.fetching_messages()
        # Now we are extending the global message list with the new_messages_from_client
        messages.extend(new_messages_from_client)
        print(messages)

        # Now we are iterating to the new_messages_from_client
        for msg_item in new_messages_from_client:
            # checking condition for the msg_item
            if msg_item == "{leave}":
                print("leaving the chat window...")
                cond=False
                #leaving the chat window...
                break



print("Calling the Main() function....")
Thread_3=Thread(target=update_messages)
Thread_3.start()
print("starting a new thread.....")

#running flask app
creating_app.run(debug=True,host="127.0.0.1")
