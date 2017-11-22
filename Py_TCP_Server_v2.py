import socket
import netifaces as ni
from netifaces import AF_INET, AF_INET6, AF_LINK
import threading

class ClientThread(threading.Thread):
    def __init__(self, client, details):
        self.client = client
        self.details = details
        threading.Thread.__init__ ( self )

    def run(self):
        print('Received connection:', self.details[0])

        while True:

            data = self.client.recv(1024)
            client_details = self.details[0]
            print("[*] Received '", data, client_details,
                  "' from the client")
            strhello = "Hello server"
            strdisconnect = "disconnect"

            if data == strhello.encode('utf-8'):
                server_reply = 'Hello client'
                self.client.sendall(
                    server_reply.encode('utf-8'))
                print("Processing done.\n[*] Reply sent")
            elif data == strdisconnect.encode('utf-8'):
                server_reply = 'Goodbye'
                self.client.sendall(
                    server_reply.encode('utf-8'))
                self.client.close()
                print('Closed connection:',
                      self.details[0])
                break
            else:
                server_reply = 'Invalid data'
                self.client.sendall(
                    server_reply.encode('utf-8'))
                print("Processing done Invalid data.\n[*] "
                      "Reply sent")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#using netifaces. Get the IP address interface eth0 
ip = ni.ifaddresses('eth0')[AF_INET][0]['addr']
print (ip)
port = 1234
address = (ip,port)
server.bind(address)
server.listen(5)

while True:
    print("[*] Started listening on ", ip, ":", port)
    client, details = server.accept()
    ClientThread(client, details).start()