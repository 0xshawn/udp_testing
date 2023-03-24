import argparse
import socket
import time

parser = argparse.ArgumentParser(description="UDP Client")
parser.add_argument(
    "-l",
    "--listen",
    type=str,
    default="127.0.0.1",
    help="IP to check connectivity",
)
parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=1234,
    help="Port to check connectivity",
)

args = parser.parse_args()
ip = args.listen
port = args.port

print(f"Check udp on {ip}:{port}")

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = b"PING"
    addr = (ip, port)

    start = time.time()
    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print(f"{data} {elapsed:.6f}s")
    except socket.timeout:
        print("REQUEST TIMED OUT")
    time.sleep(1)
