from .models import Action, Observation, Reward

class TollEnv:
    def __init__(self):
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
        view = prompts.get(task_id, "System Ready")
        return Observation(view=view, metadata={"task": task_id})

    def step(self, action: Action):
        self.step_count += 1
        cmd = action.command
        reward_val = 0.0
        done = False
        reason = "Processing..."

        if self.task_id == 0 and cmd == "open_gate":
            reward_val, done, reason = 1.0, True, "Car passed."
        elif self.task_id == 1:
            if cmd == "collect_toll":
                reward_val, reason = 0.5, "Toll collected."
            elif cmd == "open_gate":
                if self.step_count > 1:
                    reward_val, done, reason = 1.0, True, "Truck paid and passed."
                else:
                    reward_val, reason = -0.5, "Error: No payment!"
        elif self.task_id == 2:
            if cmd == "open_gate":
                reward_val, done, reason = 1.0, True, "Emergency cleared."
            else:
                reward_val, reason = -1.0, "Priority violation!"

        return Observation(view="Updated", metadata={}), Reward(value=reward_val, reasoning=reason), done, {}