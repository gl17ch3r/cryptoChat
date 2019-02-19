#!/usr/bin/python

import hashlib, os, signal, sys, socket, select, base64, ConfigParser
from Crypto.Cipher import AES

config = ConfigParser.RawConfigParser()
config.read(r'cChat.conf')
HOST = config.get('config', 'HOST')
PORT = int(config.get('config', 'PORT'))
PASSWORD = config.get('config', 'PASSWORD')
VIEW = str(config.get('config', 'VIEW'))

SOCKET_LIST = []
RECV_BUFFER = 4096

def cChat():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    SOCKET_LIST.append(server_socket)

    print "Server started on port " + str(PORT)

if __name__ == "__main__":

    sys.exit(cChat())
