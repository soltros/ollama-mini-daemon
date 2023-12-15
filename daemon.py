#!/usr/bin/env python3

import subprocess
import threading

def read_output(process):
    while True:
        output = process.stdout.readline()
        if output == '':
            break
        print(output.strip())

def run_npm():
    process = subprocess.Popen(['npm', 'run', 'dev'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Start a thread to read and print output
    output_thread = threading.Thread(target=read_output, args=(process,))
    output_thread.start()

    # Wait for a key press to terminate the program
    input("Press enter to stop the program: ")

    # Terminate the npm process
    process.kill()
    process.wait()  # Wait for the process to terminate completely

    # Wait for the output thread to finish
    output_thread.join()

if __name__ == "__main__":
    run_npm()
