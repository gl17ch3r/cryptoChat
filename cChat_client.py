#!/usr/bin/python

import base64, sys, socket, select, os, hashlib, signal
from Crypto.Cipher import AES

def sigint_handler(signum, frame):
    print '\n user interrupt ! shutting down'
    print "[info] shutting down NEURON \n\n"
    sys.exit()

signal.signal(signal.SIGINT, sigint_handler)

def hasher(key):
	hash_object = hashlib.sha512(key)
	hexd = hash_object.hexdigest()
	hash_object = hashlib.md5(hexd)
	hex_dig = hash_object.hexdigest()
	return hex_dig

def encrypt(secret,data):
	BLOCK_SIZE = 32
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	cipher = AES.new(secret)
	encoded = EncodeAES(cipher, data)
	return encoded

def decrypt(secret,data):
	BLOCK_SIZE = 32
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	cipher = AES.new(secret)
	decoded = DecodeAES(cipher, data)
	return decoded

def chat_client():
    if(len(sys.argv) < 5) :
        print '\nUsage : python cChat_client.py <hostname> <port> <password> <nick_name>\n'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    key = sys.argv[3]
    key = hasher(key)
    uname = sys.argv[4]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

if __name__ == "__main__":

	if not os.geteuid()==0:
		sys.exit("\nOnly root can run this script\n")

	sys.exit(chat_client())
