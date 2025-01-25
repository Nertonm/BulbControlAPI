import tinytuya
from pydantic import BaseModel
import os
import json

class lampada_object:
    def __init__(self, name, device_id, ip, local_key, ver):
        self.name = name
        self.lamp = tinytuya.BulbDevice(dev_id = device_id, address= ip,
                                        local_key= local_key, connection_timeout = 10, version= ver)

    def __str__(self):
        return (f"lamp_object(name={self.name}, device_id={self.lamp.id},"
                f" ip={self.lamp.address}, version={self.lamp.version}, local_key={self.lamp.local_key})")
    


def load_devices():
    lampadas = []
    file_path = os.path.join(os.path.dirname(__file__), '..', 'lampadas.json')
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            for lampada in data.get('lampadas', []):
                b = lampada_object(lampada['name'], lampada['device_id'], lampada['ip'], lampada['local_key'], lampada['ver'])
                print(f'Device {lampada["name"]} loaded.')
                lampadas.append(b)
        return lampadas
    except FileNotFoundError:
        print(f"Error: '{file_path}' file not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

class lampada_estado(BaseModel):
    name: str = ""
    state: bool = True

class lampada_color_estado(lampada_estado):
    red: int
    green: int
    blue: int

class lampada_color(BaseModel):
    red: int
    green: int
    blue: int



