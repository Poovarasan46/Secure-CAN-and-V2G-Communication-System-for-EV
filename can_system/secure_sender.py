import can
import time

bus = can.interface.Bus(channel='vcan0', interface='socketcan')

counter = 0

def send_secure():
    global counter
    counter += 1

    # Simulated secure payload (8 bytes max)
    # [ID(2B) | Counter(2B) | Signature(4B)]
    data = [
        0xAA, 0x55,                     # Fake header
        (counter >> 8) & 0xFF, counter & 0xFF,  # Counter
        0xDE, 0xAD, 0xBE, 0xEF          # Fake MAC/signature
    ]

    msg = can.Message(arbitration_id=0x123, data=data, is_extended_id=False)
    bus.send(msg)
    print("Sent:", data)

while True:
    send_secure()
    time.sleep(1)
