#! /usr/bin/env python

import Diodes.diodes as diodes
import Server.server as server


server.server_init()
data = server.server_receive_data()
server.server_terminate()


diodes.setup_GPIO()
diodes.blink_diode(data)

