import bluetooth

services = bluetooth.find_service(name="BirdBotImageTransfer")

if not services:
    raise RuntimeError("BirdBot service not found")

svc = services[0]

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((svc["host"], svc["port"]))

with open("/home/jacob/BirdBotV1/src/python/received.jpg", "wb") as f:
    while data := sock.recv(1024):
        f.write(data)

sock.close()