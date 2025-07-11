import socket 

HOST = "127.0.0.1"
PORT = 65432

while True:
    msg = input("message to send: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.sendall(msg.encode())
        if msg.lower() in ["exit", "quit"]:
            break