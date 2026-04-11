from pydantic import BaseModel
from typing import List

class Action(BaseModel):
    action: int  # 0: Allow, 1: Block, 2: Divert

class Observation(BaseModel):
    vehicle_count: int
    avg_speed: float
    current_status: str