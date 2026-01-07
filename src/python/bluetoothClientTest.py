import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("MAC_ADDRESS", 1))

with open("received.jpg", "wb") as f:
    while True:
        data = sock.recv(1024)
        if not data:
            break
        f.write(data)

sock.close()