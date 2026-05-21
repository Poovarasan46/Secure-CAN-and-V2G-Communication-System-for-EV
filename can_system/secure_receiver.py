import can

bus = can.interface.Bus(channel='vcan0', interface='socketcan')

last_counter = -1

def verify(data):
    global last_counter

    # Extract fields
    header = data[0:2]
    counter = (data[2] << 8) | data[3]
    signature = data[4:8]

    # Check header
    if header != bytearray([0xAA, 0x55]):
        print("Invalid header → spoofing detected")
        return

    # Check replay
    if counter <= last_counter:
        print("Replay attack detected")
        return

    # Check fake signature
    if signature != bytearray([0xDE, 0xAD, 0xBE, 0xEF]):
        print("MAC invalid → spoofing detected")
        return

    last_counter = counter
    print("Secure message accepted | Counter:", counter)

while True:
    msg = bus.recv()
    verify(msg.data)
