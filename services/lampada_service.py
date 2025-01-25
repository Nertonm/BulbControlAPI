import sys
import os
import json
import tinytuya
from flask import Flask, request, jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.lampada import lampada_object, lampada_estado, load_devices
import utils.colors

app = Flask(__name__)

lampadas = []
lampadaada_state = []
schemes = []


@app.route('/set_state', methods=['PUT'])
def set_lampada_state_service(estados: lampada_estado):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400

        estado = data.get('estado')
        lampada_name = data.get('name')

        if lampada_name is None:
            return jsonify({'status': 'error', 'message': 'lampada name not provided'}), 400

        for lampada in lampadas:
            for lampada_estado in lampada_estado:
                if lampada_estado['name'] == lampada_name and lampada_estado['estado'] == True:
                    lampada.turn_on

        return jsonify({'status': 'lampada not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    lampadas = load_devices()
    app.run(debug=True)