import socket, ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="charger.crt", keyfile="charger.key")

bindsocket = socket.socket()
bindsocket.bind(('localhost', 8443))
bindsocket.listen(5)

print("Charger (Server) running...")

while True:
    newsocket, fromaddr = bindsocket.accept()
    conn = context.wrap_socket(newsocket, server_side=True)
    print("Secure connection established")

    data = conn.recv(1024)
    print("Received:", data.decode())

    conn.send(b"Charging Started")
    conn.close()
