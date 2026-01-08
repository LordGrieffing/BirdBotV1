import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("2c:cf:67:af:d9:a7", 3))

with open("/home/jacob/BirdBotV1/src/python/received.jpg", "wb") as f:
    while True:
        data = sock.recv(1024)
        if not data:
            break
        f.write(data)

sock.close()