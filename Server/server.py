import socket


def handle_server():

    HOST = '192.168.1.2'
    PORT = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()

    data = conn.recv(1024)
    conn.close()

    return data