import argparse
import random
import socket

parser = argparse.ArgumentParser(description="UDP Server")
parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=1234,
    help="Port number",
)
args = parser.parse_args()
port = args.port
print(f"Listening on port: {port}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", port))
print("Server initialized and listening...")

while True:
    message, address = server_socket.recvfrom(1024)
    message = message.upper()
    if message == b"PING":
        reply = b"PONG"
    else:
        reply = message
    print(f"receive message from {address}: {message}")
    server_socket.sendto(reply, address)
