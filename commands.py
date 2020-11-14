#!/usr/bin/env python

from dotenv import load_dotenv
from dandelion import DataTXT

import speech_recognition as sr
import random
import yaml
import os

load_dotenv()

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
datatxt = DataTXT(token=os.getenv('TOKEN'))

def compare(cmd:str, cmds:map):
    best_cmd = list(cmds)[0]
    similiarity = 0
    for cmd_ in cmds:
        res = datatxt.sim(cmd_, cmd, lang='en')
        print('>', cmd_, res['similarity'])
        if res['similarity'] > similiarity:
            best_cmd = cmd_
            similiarity = res['similarity']

    return best_cmd

def listen():
    with mic as source:
        audio = r.listen(source)
    cmd = r.recognize_google(audio, language='en')
    print(cmd)
    with open('commands.yaml') as file:
        content = yaml.full_load(file)
    cmds = content.keys()
    cmd = compare(cmd, cmds)
    action = content[cmd]
    if type(action) is str:
        response = action
    if type(action) is list:
        response = random.choice(action)
    print(f"{response}")
    os.system(f"say -v Alex \"{response}\"")

if __name__=="__main__":
    listen()
    # print(os.getenv("TOKEN"))
