#! /usr/bin/env python

import Diodes.diodes as diodes
import Server.server as server


data = server.handle_server()
diodes.setupGPIO()
diodes.blink_diode(data)

