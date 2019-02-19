#!/usr/bin/python

import hashlib, os, signal, sys, socket, select, base64, ConfigParser
from Crypto.Cipher import AES

def sigint_handler(signum, frame):
    print '\nShutting down criptoChat...\n'
    sys.exit()

signal.signal(signal.SIGINT, sigint_handler)

def hasher(key):
	hash_object = hashlib.sha512(key)
	hexd = hash_object.hexdigest()
	hash_object = hashlib.md5(hexd)
	hex_dig = hash_object.hexdigest()
	return hex_dig

config = ConfigParser.RawConfigParser()
config.read(r'cChat.conf')
HOST = config.get('config', 'HOST')
PORT = int(config.get('config', 'PORT'))
PASSWORD = config.get('config', 'PASSWORD')
VIEW = str(config.get('config', 'VIEW'))

key = hasher(PASSWORD)

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
