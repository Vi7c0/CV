#this is code for a TCP client.
#Why do Pentesters need a TCP Client.
#Pentesters offen do not have the luxury to connect to internet. So a TCP Client will give that luxury.

import socket

host = "www.google.com"
port = 80

#AF_INET indecates that it will be using a IPv4 address. And SOCK_STREAM indecates that this code will be a TCP Client.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Here we are connecting the client to the sever.
client.connect((host, port))

#This is the data that will be sent in bytes.
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#Here we get our data back.
response = client.recv(4096)

#This prints out the decoded data and closes connection.
print(response.decode())
client.close()
