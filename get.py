import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8000))

s.send(b'GET / HTTP/1.0\n\n')

# while True:
#     resp = s.recv(1024)

#     if not resp:
#         break

#     print(resp)

s.close()
