import sys
import os
from fastapi import FastAPI, Request

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.lampada import lampada_object, lampada_estado, load_devices
from controllers.lampada_controller import router as lamp_router

app = FastAPI()

lampadas = []
lampadaada_state = []
schemes = []

app.include_router(lamp_router)

@app.put('/set_state')
def set_lampada_estado(request: Request, estados: lampada_estado):
    try:
        data = request.json()
        if not data:
            return {'status': 'error', 'message': 'No data provided'}, 400

        estado = data.get('estado')
        lampada_name = data.get('name')

        if lampada_name is None:
            return {'status': 'error', 'message': 'lampada name not provided'}, 400

        for lampada in lampadas:
            for lampada_estado in lampada_estado:
                if lampada_estado['name'] == lampada_name and lampada_estado['estado'] == True:
                    lampada.turn_on

        return {'status': 'lampada not found'}, 404
    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 500

if __name__ == '__main__':
    lampadas = load_devices()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)