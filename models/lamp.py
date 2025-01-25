
from pydantic import BaseModel

from lamp_control import *

class lamp_states(BaseModel):
    name: str = ""
    state: bool = True

class lamp_color(BaseModel):
    red: int
    green: int
    blue: int

class lamp_color_states(lamp_state):
    red: int
    green: int
    blue: int


