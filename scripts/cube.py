from pycube import Cube
import sys, select, getpass, os, time, getopt, hashlib

try:
    mode = sys.argv[1]
except IndexError as ier:
    sys.stdout.write("Error: Did you forget encrypt/decrypt?\n")
    sys.exit(1)

try:
    key = sys.argv[2]
except IndexError as ier:
    key = getpass.getpass("Enter key: ")

if mode == "encrypt":
    data = raw_input("Enter text to encrypt: ")
    cipher_text = Cube(key).encrypt(data)
    sys.stdout.write(cipher_text+"\n")
elif mode == "decrypt":
    data = raw_input("Enter text to decrypt: ")
    plain_text = Cube(key).decrypt(data)
    sys.stdout.write(plain_text+"\n")
