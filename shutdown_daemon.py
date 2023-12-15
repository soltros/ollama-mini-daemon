#!/usr/bin/env python3

import socket

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5000))
        s.sendall(command.encode())

if __name__ == "__main__":
    send_command("shutdown")

