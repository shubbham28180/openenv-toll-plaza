import random
from .models import Action, Observation

class TollPlazaEngine:
    def __init__(self):
        self.step_count = 0

    def reset(self):
        self.step_count = 0
        return Observation(
            vehicle_count=random.randint(0, 50),
            avg_speed=40.0,
            current_status="Normal"
        )

    def step(self, action: Action):
        self.step_count += 1
        # Simple logic for toll simulation
        status = "Congested" if action.action == 1 else "Clear"
        
        obs = Observation(
            vehicle_count=random.randint(10, 100),
            avg_speed=random.uniform(20.0, 60.0),
            current_status=status
        )
        
        reward = 1.0 if action.action == 0 else -1.0
        done = self.step_count >= 10
        info = {"details": "Toll simulation step"}
        
        return obs, reward, done, info