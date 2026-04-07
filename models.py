from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    step_number: int
    queue_lengths: List[int]
    open_lanes: int
    average_wait_time: float
    emergency_vehicle_waiting: bool
    message: str

class Action(BaseModel):
    action_type: str
    lane_id: Optional[int] = None

class Reward(BaseModel):
    score: float
    reason: str