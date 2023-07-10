from socket import AF_INET
from socket import socket
from socket import SOCK_STREAM
from threading import Thread
from threading import Lock
import time


class Client:
    client_port_number = 5500
    client_host = "localhost"
    size = 1024

    def __init__(self, name):
        print("creating a socket for client...")
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        #creating a socket for client
        self.list_messages = list()
        print(self.list_messages)
        self.client_socket.connect((self.client_host, self.client_port_number))
        self.sharing_message(name)
        #sharing for sending messages
        Thread(target=self.collect_messages).start()
        #new thread is staring now for recieve the messages
        print("locking for lock the thread until it finishes its operations...")
        self.lock = Lock()

    def collect_messages(self):
        bool4=True
        while bool4:
            try:
                msg = self.client_socket.recv(self.size)
                msg=msg.decode()
                #using locks for threads
                self.lock.acquire()
                print("aquiring the lock...")
                print()
                self.list_messages.append(msg)
                print(msg)
                self.lock.release()
                print("releasing the lock...")
            except Exception as e:
                bool4=False
                print("exception with threads+4", e)


    def sharing_message(self, msg):
        #used to share the messages
        try:
            print("sending the messages..")
            self.client_socket.send(msg.encode(encoding="utf8", errors="ignore"))
            if msg == "{leave}":
                print("closing the socket")
                self.client_socket.close()
                #leaving the chat room
        except Exception as e:
            self.client_socket = socket(AF_INET, SOCK_STREAM)
            print("trying to connect...")
            self.client_socket.connect((self.client_host, self.client_port_number))
            #connect back to port
            print("exception with threads+4", e)

    def fetching_messages(self):
        print("bringing the messages to the screen")
        copy_messages = self.list_messages[:]
        print(copy_messages)
        print("securing memory by using locks")
        self.lock.acquire()
        print("aquiring lock...")
        self.list_messages = []
        #making the messages list empty
        print(self.list_messages)
        self.lock.release()
        print("releasing the lock...")
        #other thread can connect now
        return copy_messages
