#!/usr/bin/env python

from pynput.keyboard import Listener
from commands import listen

import os
import logging
import string

def key_handler(key):
    logging.info(key)
    parse(key)

keys = []
def parse(key):
    if len(keys) >= 2:
        keys.pop(0)
    keys.append(key)
    print(key.__dict__)

    if not hasattr(keys[0], '_name_'):
        return
    if keys[0]._name_ != 'alt':
        return
    if not hasattr(keys[1], 'char'):
        return
    if keys[1].char != '©':
        return
    print('listening now')
    listen()

def keylog():
    username = os.getlogin()
    logging_directory = "."
    logging.basicConfig(filename=f"{logging_directory}/logs.txt",
                        level=logging.DEBUG, format="%(asctime)s: %(message)s")

    with Listener(on_press=key_handler) as listener:
        listener.join()

if __name__=="__main__":
    keylog()
