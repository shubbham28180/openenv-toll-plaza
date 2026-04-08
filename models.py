from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class Observation(BaseModel):
    view: str
    metadata: Dict[str, Any]

class Action(BaseModel):
    command: str
    args: Optional[Dict[str, Any]] = None

class Reward(BaseModel):
    value: float  # Must be 0.0 to 1.0
    reasoning: str