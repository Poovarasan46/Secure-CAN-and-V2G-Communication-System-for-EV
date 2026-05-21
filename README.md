# Secure CAN and V2G Communication System for EV

## Overview

This project presents a simulation-based automotive cybersecurity framework focused on securing Controller Area Network (CAN) communication and Vehicle-to-Grid (V2G) communication in electric vehicles. The system demonstrates common vulnerabilities in traditional CAN networks and implements security mechanisms such as authentication, encryption, replay protection, spoofing detection, and TLS-based secure communication.

The project was developed as part of the **Network and Communication for Connected Vehicles** elective subject.

---

## Objectives

- Simulate secure CAN communication using SocketCAN
- Detect spoofing, replay, and Denial of Service (DoS) attacks
- Implement authentication mechanisms for CAN messages
- Secure Vehicle-to-Grid communication using TLS
- Analyze encrypted traffic using Wireshark
- Demonstrate practical automotive cybersecurity concepts

---

# Project Architecture

```text
                     +---------------------------+
                     |      Virtual CAN (vcan0) |
                     +---------------------------+
                              |
         -------------------------------------------------
         |                                               |
+-------------------+                     +-----------------------+
| Secure CAN Sender |                     | Secure CAN Receiver   |
|     (Python)      |-------------------> |  Validation Engine    |
+-------------------+                     +-----------------------+
                                                     |
                                                     v
                                       +---------------------------+
                                       | Attack Detection Module   |
                                       | Spoofing / Replay / DoS   |
                                       +---------------------------+

==================================================================

                Vehicle-to-Grid (V2G) Communication

+-------------------+        TLS Encrypted       +------------------+
| EV Client System  | <------------------------> | Charging Server  |
|   (Python TLS)    |                            |   (Python TLS)   |
+-------------------+                            +------------------+

==================================================================

Supporting Technologies:
- Python
- SocketCAN
- OpenSSL
- Wireshark
- Linux Virtual CAN Interface
