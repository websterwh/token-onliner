
from requests import get
import threading
from discord.ext import commands
import discord
import pyautogui
import time
import re
import http.client
import random
import json
import requests
from threading import Thread
from requests import Session
import base64
import string
import sys
import os
import websocket
from os import system
import discum

os.system("cls")
title = 'Onliner'
system(f'title {title}')
tokens = open('tokens.txt', 'r').read().splitlines()

def activity(token, act):
    print('[+] Activity Status')
    while True:
        ws = websocket.WebSocket()
        actt = 'Online'
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        gjs = {'name': act,
                    'type': 0}
        auth = {'op': 2,
                'd': {'token': token,
                    'properties': {'$os': sys.platform,
                                    '$browser': 'RTB',
                                    '$device': f"{sys.platform} Device"},
                    'presence': {'game': gjs,
                                'status': actt,
                                'since': 0,
                                'afk': False}},
                's': None,
                't': None}
             
        ws.send(json.dumps(auth))
        time.sleep(20)
        print('[+] Activity Status')


#text = input('Activity Status: ')

for token in tokens:
    threading.Thread(target=activity, args=(token, '')).start()

