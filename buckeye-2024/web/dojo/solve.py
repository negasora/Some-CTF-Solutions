import requests

import websocket
import json

import time
from threading import Thread

import base64

from numpy.random import Generator, PCG64



import random
import socket
import struct


game_id = 1102683355
expected = [
35,
1,
27,
34,
99,
29,
]

LOCAL = False

if LOCAL:
    host = "127.0.0.1:8080"
    proto_suffix = ''
else:
    host = "dojo.challs.pwnoh.io"
    proto_suffix = 's'
url = f"http{proto_suffix}://{host}/api/new"

ws_url = f"ws{proto_suffix}://{host}/api/ws"

plunder_url = f"http{proto_suffix}://{host}/api/plunder"
dodge_url = f"http{proto_suffix}://{host}/api/dodge"
attack_url = f"http{proto_suffix}://{host}/api/attack"


s = requests.Session()

r = s.get(url)
print(r.text)

jwt = s.cookies['jwt']

game_id = json.loads(base64.b64decode(jwt.split('.')[1] + '==').decode())['game_id']

def fake_ip_headers():
    random_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    return {
    'True-Client-IP': random_ip,
    'X-Real-IP': random_ip,
    'X-Forwarded-For': random_ip,
    }

"""
can only send 2 requests a second
plunder until we have 800

on signal, wait 500ms then dodge

otherwise attack then immediately dodge
"""

import subprocess

lost = False

command_queue: list[str] = []

def on_open(ws: websocket.WebSocket):
    def run(*args):
        global lost
        plundered = 0
        while not lost:
            if len(command_queue) > 0:
                cmd = command_queue.pop(0)
                if cmd == 'dodge':
                    print('dodging')
                    r = s.get(dodge_url)
            # if there's a command in the queue, send it
            if plundered < 800:
                print('plundering')
                r = s.get(plunder_url, headers=fake_ip_headers())
                print(r.text)
                data = r.json()
                if data['status'] == 'success':
                    plundered = data['total']
                    print('plundered, at', plundered)
            else:
                print('attacking')
                r = s.get(attack_url, headers=fake_ip_headers())
                data = r.json()
                if data['status'] == 'error':
                    print('attack failed')
                    exit(0)
                print(data)
                if data['status'] == 'success':
                    print('plundered, at', plundered)

    Thread(target=run).start()

def on_message(ws: websocket.WebSocket, message: str):
    global command_queue, lost
    print(message)
    data = json.loads(message)
    action = data['action']
    if action == 'lose':
        print('we lost')
        lost = True
        exit(0)
    if data['action'] == 'signal':
        print("signal, queueing dodge...")
        command_queue.append('dodge')
    #else:
    #    # dodge then attack

    print(message)

wsapp = websocket.WebSocketApp(ws_url, cookie=f"jwt={jwt}", on_message=on_message)

wsapp.on_open = on_open

wsapp.run_forever()
