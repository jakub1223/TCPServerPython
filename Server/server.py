import socket


HOST = '127.0.0.1' #''192.168.1.2
PORT = 12345
conn = 0.0
address = 0.0


def init():
    global conn
    global address
    global HOST
    global PORT

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()


def receive_data():
    global conn
    data = conn.recv(1024)
    return data


def send_data(data_to_send):
    global conn
    conn.sendall(bytearray(data_to_send, "utf-8"))


def terminate():
    global conn
    conn.close()