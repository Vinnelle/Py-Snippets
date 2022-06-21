import socket
import subprocess
import sys

# Clear the screen
subprocess.call('cls', shell=True)

# Get the target IP
ip = input("Enter the IP Address: ")

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data to the target
s.sendto(bytes("Hello, world!", "utf-8"), (ip, 80))

# Receive some data from the target
data, addr = s.recvfrom(1024)

# Print out the received data
print(data.decode("utf-8"))
