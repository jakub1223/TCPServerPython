from serial import Serial

#9600 bauds, 8 bits, on my Ubuntu it's ttyS0,but I'm not using it here


def make_connection():
    serial_port = Serial("/dev/ttyAMA0")

    if serial_port.isOpen() == False:
        serial_port.open()
        print("Port opened")

    data_to_send = input("what do you want to send?")
    serial_port.write(bytes(data_to_send, 'UTF-8'))
    data_received = serial_port.read()
    print('Received: {0}'.format(data_received))
