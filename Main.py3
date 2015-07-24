#! /usr/bin/env python3


import Diodes.diodes as diodes
import Server.server as server
import Microcontroller.UART as UART
import subprocess
import threading


def setup():
    server.init()
    diodes.setup_GPIO()


class DataGatheringAndStorage(threading.Thread):
    def run(self):
        #debug and developement purposes. will handle microcontroller UART conneciton
        #and data storage
        subprocess.call('Bash/bash_data_handle.sh write', shell=True)
        #UART and any other communication will be dealt with at the final stage of the project.
        #As for now it has undergone simple tests to check whether it works.
        ##diodes.blink_diode()


class WebService(threading.Thread):
    def run(self):
        #debug and developement purposes. will handle web connections
        message_to_send = 'Hello from python'
        data = server.receive_data()
        #TODO received data handling
        server.send_data(message_to_send)
        server.terminate()


#main flow here

setup()

#TODO this needs to be in a loop

data_gathering_thread = DataGatheringAndStorage()
web_storage_thread = WebService()
data_gathering_thread.start()
web_storage_thread.start()

