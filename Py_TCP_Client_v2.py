import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.2.110',1234)) #((Ip,port)) of TCP server
while True:

    data = input('Type your message!: ')
    print("Message typed :",data)

    if data == "disconnect":
        client.sendall(data.encode('utf-8'))
        print("Message:'", data, "' was send.")
        print(client.recv(1024))
        client.close()
        break
    else:
        client.sendall(data.encode('utf-8'))
        print("Message: ", data, "was send.")
        print(client.recv(1024))




