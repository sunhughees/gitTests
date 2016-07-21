import socket

s = socket.socket()

host = socket.gethostname()
port = 8088

s.connect((host, port))


message = '{"Hello": "Echo!"}'

s.sendall(message)

print s.recv(2048)
print s.recv(2048)
