import random
from .models import Action, Observation

class TollPlazaEngine:
    def __init__(self):
        self.step_count = 0

    # reset ke aage async lagao
    async def reset(self):
        self.step_count = 0
        return Observation(
            vehicle_count=random.randint(0, 50),
            avg_speed=40.0,
            current_status="Normal"
        )

    # step ke aage async lagao
    async def step(self, action: Action):
        self.step_count += 1
        status = "Congested" if action.action == 1 else "Clear"
        
        obs = Observation(
            vehicle_count=random.randint(10, 100),
            avg_speed=random.uniform(20.0, 60.0),
            current_status=status
        )
        
        return obs, 1.0, self.step_count >= 10, {"step": self.step_count}

    # Ye function missing tha, isliye 500 Error aa raha tha
    def close(self):
        pass