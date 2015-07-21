#! /usr/bin/env python

import Diodes.diodes as diodes
import Server.server as server


server.init()
data = server.receive_data()
server.terminate()


diodes.setup_GPIO()
diodes.blink_diode(data)
