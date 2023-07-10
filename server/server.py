from socket import AF_INET
from socket import socket
from socket import SOCK_STREAM
from threading import Thread
from Users import Users
import time


host_name = "localhost"
size = 1024
port_no = 5500
users = []
comm_server = socket(AF_INET, SOCK_STREAM)
comm_server.bind((host_name, port_no))  # set up server
comm_server.listen(10)
print("Setting the connections...")

def client_messages(user):

    print("waiting for client messages...")
    socket_obj = user.client
    #user trying to connect to the server
    name = socket_obj.recv(size).decode("utf8")
    print(f" user name is:{name}")
    user.assign_name(name)
    # broadcast(msg, "")  # broadcast welcome message
    # for person in users:
    #     client = person.client
    #     try:
    #
    #         client.send(str(name + msg.decode("utf8")).encode(encoding="utf8", errors="ignore"))
    #     except Exception as e:
    #         print("[EXCEPTION]+3", e)
    bool3=True
    while bool3:
        try:
            msg = socket_obj.recv(size)
            print(type(msg))
            # print(msg+"1")
            if msg == "{leave}".encode(encoding="utf8",errors="ignore") :
                print("disconectting...")
                socket_obj.close()
                #closing the object
                users.remove(user)
                #removing the user
                print(f"{name} left the chat")
                for item in users:
                    #broadcasting the messages to each client
                    client = item.user
                    try:

                        client.send(str(name + msg.decode("utf8")).encode(encoding="utf8",errors="ignore"))
                    except Exception as e:
                        print("exception with threads+3", e)

                print(f" {name} is disconnecting")
                break
            else:

                print("sending messages to all the users")
                for item in users:
                    client = item.client
                    try:
                        msg=msg.decode("utf8")
                        # name=name.decode("utf8")
                        print(type(msg))
                        print(type(name))
                        client.send((name+": "+ msg).encode(encoding="utf8",errors="ignore"))
                    except Exception as e:
                        print(type(msg))
                        print(type(name))
                        client.send((name + ": " + msg).encode(encoding="utf8", errors="ignore"))
                        # print("[EXCEPTION]+ 0", e)
                print(f"{name}: ", msg)

        except Exception as e:
            print("exception with threads+2", e)
            bool3=False


def setting_connection():
    bool1 = True
    while bool1:
        try:
            addr, obj = comm_server.accept()
            print("recieving the address of the users")
            #comm.accept() will wait for any connections are trying to connect
            user = Users(addr, obj)
            print("creating the user class")
            #creating the user for connection
            Thread_2 = Thread(target=client_messages, args=(user,))
            users.append(user)
            Thread_2.start()
        except Exception as e:
            bool1 = False
            print("exception with threads+1", e)


Thread1 = Thread(target=setting_connection)
print("starting the thread1... for main server")
Thread1.start()
#thread will be blocked untill client or users are joined
Thread1.join()
#close the server when users leave the chat window
comm_server.close()