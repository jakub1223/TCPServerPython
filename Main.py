#! /usr/bin/env python

import Diodes.diodes as diodes
import Server.server as server


def setup():
    server.init()
    diodes.setup_GPIO()


def loop():

    message_to_send = 'Hello from python'

    data = server.receive_data()
    server.send_data(message_to_send)
    diodes.blink_diode(data)

    server.terminate()

setup()
loop()