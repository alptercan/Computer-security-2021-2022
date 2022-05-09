import sys
import os
from common import *
from const import *

flag = sys.argv[1]
player = os.path.basename(sys.argv[0]).split('.', 1)[0]
bobSocket, bobAes = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
aliceSocket, aliceAes = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)

Dialog("print").info("Waiting for message...")

#Bob to Alice.
bobToAlice = receive_and_decrypt(aliceAes, aliceSocket)

Dialog("print").chat('Bob said:"{}"'.format(bobToAlice))

if flag == "--relay":
    encrypt_and_send(bobToAlice, bobAes, bobSocket)
elif flag == "--break-heart":
    encrypt_and_send(BAD_MSG['bob'], bobAes, bobSocket)
elif flag == "--custom":
    Dialog("print").prompt("Please input message...")
    to_send = input()
    encrypt_and_send(to_send, bobAes, bobSocket)

#Now same with Alice to Bob.

aliceToBob = receive_and_decrypt(bobAes, bobSocket)

Dialog("print").chat('Alice said:"{}"'.format(aliceToBob))

if flag == "--relay":
    encrypt_and_send(aliceToBob, aliceAes, aliceSocket)
elif flag == "--break-heart":
    encrypt_and_send(BAD_MSG['alice'], aliceAes, aliceSocket)
elif flag == "--custom":
    Dialog("print").prompt("Please input message...")
    to_send = input()
    encrypt_and_send(to_send, aliceAes, aliceSocket)

