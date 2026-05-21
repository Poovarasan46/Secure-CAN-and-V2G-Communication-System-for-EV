import socket, ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

sock = socket.socket()
secure_sock = context.wrap_socket(sock, server_hostname='localhost')

secure_sock.connect(('localhost', 8443))

secure_sock.send(b"Start Charging Request")

data = secure_sock.recv(1024)
print("Server Response:", data.decode())

secure_sock.close()
