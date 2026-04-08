from pydantic import BaseModel
from typing import Optional, Dict, Any

class Action(BaseModel):
    command: str
    args: Optional[Dict[str, Any]] = None

class Observation(BaseModel):
    view: str
    metadata: Dict[str, Any]

class Reward(BaseModel):
    value: float
    reasoning: str