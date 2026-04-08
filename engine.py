from models import Observation, Reward, Action

class TollEnv:
    def __init__(self):
        self.state = "Idle"
        self.task_id = 0
        self.step_count = 0

    def reset(self, task_id: int = 0):
        self.task_id = task_id
        self.step_count = 0
        
        prompts = {
            0: "A standard Sedan is at the gate. Action: open_gate",
            1: "A heavy Truck is at the gate. Toll: $20. Actions: collect_toll, open_gate",
            2: "An Ambulance with sirens is approaching. Actions: open_gate"
        }
        self.state = prompts.get(task_id, "System Ready")
        return Observation(view=self.state, metadata={"task": task_id})

    def step(self, action: Action):
        self.step_count += 1
        cmd = action.command
        args = action.args or {}
        
        reward_val = 0.0
        done = False
        reason = "Processing action..."

        # Task 0: Easy (Car)
        if self.task_id == 0:
            if cmd == "open_gate":
                reward_val = 1.0
                done = True
                reason = "Car passed successfully."

        # Task 1: Medium (Truck)
        elif self.task_id == 1:
            if cmd == "collect_toll":
                reward_val = 0.5
                reason = "Toll collected. Now open the gate."
            elif cmd == "open_gate":
                if self.step_count > 1: # Assumes they collected toll first
                    reward_val = 1.0
                    done = True
                    reason = "Toll paid and truck passed."
                else:
                    reward_val = -0.5
                    reason = "Error: Truck passed without paying!"

        # Task 2: Hard (Emergency)
        elif self.task_id == 2:
            if cmd == "open_gate":
                reward_val = 1.0
                done = True
                reason = "Emergency vehicle cleared immediately."
            elif cmd == "collect_toll":
                reward_val = -1.0
                reason = "Penalty: Never charge an ambulance!"

        reward = Reward(value=reward_val, reasoning=reason)
        return Observation(view="Gate Status Updated", metadata={}), reward, done, {}