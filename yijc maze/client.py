from http import client
import socket 

clientsocket = socket.socket()
clientsocket.connect(('127.0.0.1',6789))



while True:
    if '\n' in clientsocket.recv(1024).decode():
        print(clientsocket.recv(1024).decode())
    choice = input('Enter U(p), D(own), L(eft), R(ight) or Q(uit) : ').encode()
    clientsocket.sendall(choice)
    message = clientsocket.recv(1024).decode()
    print(message)
    

       
clientsocket.close() 
