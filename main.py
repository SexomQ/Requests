import socket
from pprint import pprint
# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys 
from bs4 import BeautifulSoup

### Connect to web server and get the response
try: 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	print ("Socket successfully created")
except socket.error as err: 
	print ("socket creation failed with error %s" %(err))

# default port for socket 
port = 80
host = 'www.bing.com'

try: 
	host_ip = socket.gethostbyname(host) 
except socket.gaierror: 

	# this means could not resolve the host 
	print ("there was an error resolving the host")
	sys.exit() 

print ("Ip address of web engine is %s" %(host_ip))

# connecting to the server 
s.connect((host_ip, port)) 

print (f"You has successfully connected to {host} on port == {port}")

# send data to the server
# s.sendall((f"GET / HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n").encode("utf-8"))

# receive data from the server and decoding to get the string.
# response = b""
# while True:
#     chunk = s.recv(4096)
#     if len(chunk) == 0:     # No more data received, quitting
#         break
#     response = response + chunk

# pprint(response.decode("latin-1"))

### Search for a term on bing
s.sendall((f"GET /search?q=python HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n").encode("utf-8"))

response = b""
while True:
    chunk = s.recv(4096)
    if len(chunk) == 0:     # No more data received, quitting
        break
    response = response + chunk
	
# pprint(response.decode("latin-1"))

# get first 10 responses from google search
soup = BeautifulSoup(response, "html.parser")
print(soup.prettify())


# close the connection 
s.close() 
