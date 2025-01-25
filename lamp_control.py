from flask import Flask, request

import colors

import tinytuya
import time
import os
import sys
import random
import json

from models.lamp import lamp_states

app = Flask(__name__)

lamp_state : lamp_states = []

class lamp_object:
    def __init__(self, name, device_id, ip, local_key, ver):
        self.name = name
        self.lamp = tinytuya.BulbDevice(dev_id = device_id, address= ip,
                                        local_key= local_key, connection_timeout = 10, version= ver)

    def __str__(self):
        return (f"lamp_object(name={self.name}, device_id={self.lamp.id},"
                f" ip={self.lamp.address}, version={self.lamp.version}, local_key={self.lamp.local_key})")
lamps = []
schemes = []

def load_devices():
    with open('lamps.json', 'r') as f:
        data = json.load(f)
        for lamp in data['lamps']:
            b = lamp_object(lamp['name'], lamp['device_id'], lamp['ip'], lamp['local_key'], lamp['ver'])
            print(b)
            print('Device %s' % (lamp['name']))
            lamps.append(b)

load_devices()

@app.route('/set_state', methods=['PUT'])
def set_power_state():
    data = request.get_json()
    state = data.get('state', False)
    lamp_name = data.get('name', None)

    if lamp_name:
        for l in lamps:
            if l.name == lamp_name:
                try:
                    l.lamp.set_status(True if state else False)
                    return {'status': 'success'}
                except Exception as e:
                    return {'status': 'error', 'message': str(e)}, 500
        return {'status': 'lamp not found'}, 404
    return {'status': 'name not provided'}, 400

if __name__ == '__main__':
    load_devices()
    app.run(debug=True)