# Imports
import bluetooth

# Label socket
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", 3))
server_sock.listen(1)


port = server_sock.getsockname()[1]
print("Listening on RFCOMM port", port)

# Label Client
client_sock, address = server_sock.accept()
print("Connected from", address)

# Send Files

with open("/home/rain/BirdBotV1/image_repo/testBlue.jpg", "rb") as f:
    while chunk := f.read(1024):
        client_sock.send(chunk)

client_sock.close()
server_sock.close()