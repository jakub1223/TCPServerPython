#! /usr/bin/env python3


import Diodes.diodes as diodes
import Server.server as server
import subprocess
import threading
import time


def setup():
    server.init()
    diodes.setup_GPIO()


def loop():

    message_to_send = 'Hello from python'

    data = server.receive_data()
    server.send_data(message_to_send)
    diodes.blink_diode(data)

    server.terminate()


class DataGatheringAndStorage(threading.Thread):
    def run(self):
        #debug and developement purposes. will handle microcontroller UART conneciton
        #and data storage
        subprocess.call('bash Bash/bash_data_handle.sh write', shell=True)


class WebService(threading.Thread):
    def run(self):
        #debug and developement purposes. will handle web connections
        subprocess.call('bash Bash/temp.sh', shell=True)


data_gathering_thread = DataGatheringAndStorage()
web_storage_thread = WebService()
data_gathering_thread.start()
web_storage_thread.start()

#setup()
#loop()