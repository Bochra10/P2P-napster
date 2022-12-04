import socket
import pickle
from threading import Semaphore
import constants
from Server.controller import *

class Server : 
    def __init__(self,port=PORT,host=HOST,  max_num_connections=5):
        self.host = host
        self.semaphore = Semaphore(max_num_connections)  # Handles threads synchronization for critical sections.
        self.port = int(port)  # the port it will listen to
        self.sock = socket()  # socket for incoming calls
        self.sock.bind((HOST, self.port))  # bind socket to an address
        self.sock.listen(max_num_connections)  # max num of connections
        self.listOfLists = list()  # init: no lists to manage
        print( "[*] Started listening on", self.host, ":", self.port)
        
    def run(self):
        while True:
            (conn, addr) = self.sock.accept()  # accept incoming call
            print( "[*] Got a connection from ", addr[0], ":", addr[1])
            data = conn.recv(1024)  # fetch data from peer
            request = pickle.loads(data)  # unwrap the request
            print ("[*] Request after unwrap", request)
            if request[0] == REGISTER:  # create a list
                self.semaphore.acquire()
                register(conn, self.listOfLists) 
                self.semaphore.release()

            elif request[0] == APPEND:  # append request
                self.semaphore.acquire()
                append(conn, request, self.listOfLists)
                self.semaphore.release()

            elif request[0] == GETVALUE:  # read request
                list_id = request[1]  # fetch list_id
                result = self.listOfLists[list_id]  # get the elements
                conn.send(pickle.dumps(result))  # return the list
            # -
            elif request[0] == STOP:  # request to stop
                print (self.setOfLists)
                conn.close()  # close the connection  #-
                break  # -
            elif request[0] == SEARCH:
                self.semaphore.acquire()
                found_boolean, file_object = search(request[1], self.listOfLists)
                if found_boolean:
                    conn.send(pickle.dumps([found_boolean, file_object]))
                else:
                    conn.send(pickle.dumps([found_boolean]))
                self.semaphore.release()
    