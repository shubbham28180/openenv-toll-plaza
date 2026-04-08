from models import Observation, Reward, Action

class TollEnv:
    def __init__(self):
        self.state = "Idle"
        self.task_id = 0

    def reset(self, task_id: int):
        self.task_id = task_id
        prompts = {
            0: "Car at gate. Action needed: open_gate",
            1: "Truck at gate. Action needed: collect_20, open_gate",
            2: "Ambulance at gate. Action needed: open_gate"
        }
        self.state = prompts.get(task_id, "Unknown Task")
        return Observation(view=self.state, metadata={"task": task_id})

    def step(self, action: Action):
        # Grader Logic: Easy (0), Medium (1), Hard (2)
        reward_val = 0.0
        if self.task_id == 0 and action.command == "open_gate":
            reward_val = 1.0
        elif self.task_id == 1 and action.command == "collect_20":
            reward_val = 0.5 # Partial Progress
        elif self.task_id == 2 and action.command == "open_gate":
            reward_val = 1.0 # Priority Vehicle
            
        reward = Reward(value=reward_val, reasoning="Action evaluated")
        return Observation(view="Gate Processed", metadata={}), reward, True, {}