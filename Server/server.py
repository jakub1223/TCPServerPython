import socket


HOST = '127.0.0.1'  #192.168.1.2
PORT = 12345
conn = 0.0
address = 0.0


def server_init():
    global conn
    global address

    HOST = '192.168.1.2'
    PORT = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()


def server_receive_data():
    data = conn.recv(1024)
    return data


def server_terminate():
    global conn
    conn.close()

    data = conn.recv(1024)
    conn.close()

    return data
