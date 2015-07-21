#! /usr/bin/env python

import Diodes.diodes as diodes
import Server.server as server

message_to_send = 'Hello from python'
server.init()
data = server.receive_data()
server.send_data(message_to_send)
server.terminate()


diodes.setup_GPIO()
diodes.blink_diode(data)
