import socket


<<<<<<< HEAD
HOST = '127.0.0.1'  #192.168.1.2
PORT = 12345
conn = 0.0
address = 0.0


def server_init():
    global conn
    global address
=======
def handle_server():

    HOST = '192.168.1.2'
    PORT = 12345

>>>>>>> 60725894a9cd4ceb65bf1b44aad98e810670ebb7
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, address = s.accept()

<<<<<<< HEAD

def server_receive_data():
    data = conn.recv(1024)
    return data


def server_terminate():
    global conn
    conn.close()
=======
    data = conn.recv(1024)
    conn.close()

    return data
>>>>>>> 60725894a9cd4ceb65bf1b44aad98e810670ebb7
