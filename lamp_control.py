import colors

import tinytuya
import time
import os
import sys
import random
import json
import flask

# Set up the device
class bulbs:
    def __init__(self, name, device_id, ip, local_key, ver):
        self.name = name
        self.bulb = tinytuya.BulbDevice(device_id, ip, local_key, ver)

bulb = []
schemes = []

def load_bulbs():
    with open('bulbs.json', 'r') as f:
        data = json.load(f)
        for bulb in data['bulbs']:
            b = bulbs(bulb['name'], bulb['device_id'], bulb['ip'], bulb['local_key'], bulb['ver'])
            bulb.append(b)

