#!/usr/bin/env python3

import socket

def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Timeout after 5 seconds if the server does not respond
            s.connect(('localhost', 5000))
            s.sendall(command.encode())
            # Optional: Wait for a response from the server
            # response = s.recv(1024)
            # print(f"Response from server: {response.decode()}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_command("shutdown")
