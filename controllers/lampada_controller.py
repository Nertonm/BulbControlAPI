from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LampState(BaseModel):
    name: str
    estado: bool

@router.get('/hello')
def hello_world():
    return 'Hello, World!'

@router.put('/set_estado')
def set_lamp_state_route(data: LampState):
    try:
        # Simulating the set_lampada_estado function
        if data.name and data.estado is not None:
            return {"status": "success", "message": f"Lamp {data.name} set to {data.estado}"}
        else:
            raise HTTPException(status_code=400, detail="Invalid data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))