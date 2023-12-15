#!/usr/bin/env python3

import socket
import subprocess
import threading
import os
import sys
import signal

def run_command():
    process = subprocess.Popen(["ollama", "serve"])
    return process

def handle_client(client_socket, command_process):
    with client_socket:
        while True:
            data = client_socket.recv(1024).decode()
            if data.lower() == 'shutdown':
                command_process.terminate()
                sys.exit(0)

def start_server(command_process):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen()

    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, command_process))
        client_thread.start()

def daemonize():
    if os.fork() > 0:
        sys.exit(0)

    os.chdir('/')
    os.setsid()
    os.umask(0)

    if os.fork() > 0:
        sys.exit(0)

    sys.stdout.flush()
    sys.stderr.flush()
    with open('/dev/null', 'rb') as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open('/dev/null', 'ab') as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
        os.dup2(f.fileno(), sys.stderr.fileno())

    def on_sigterm(signum, frame):
        sys.exit(0)

    signal.signal(signal.SIGTERM, on_sigterm)

def main():
    daemonize()

    process = run_command()
    start_server(process)

if __name__ == "__main__":
    main()

