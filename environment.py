from models import Observation, Action, Reward

class TollPlazaEnv:
    def __init__(self):
        self.max_steps = 10
        self.reset()

    def reset(self):
        self.step_count = 0
        self.queue_lengths = [30, 5, 4, 6]
        self.open_lanes = 4
        self.emergency_vehicle_waiting = False

        return self._get_obs()

    def _get_obs(self):
        avg_wait = sum(self.queue_lengths) / len(self.queue_lengths)

        return Observation(
            step_number=self.step_count,
            queue_lengths=self.queue_lengths,
            open_lanes=self.open_lanes,
            average_wait_time=avg_wait,
            emergency_vehicle_waiting=self.emergency_vehicle_waiting,
            message="Manage the toll plaza traffic"
        )

    def state(self):
        return {
            "step": self.step_count,
            "queues": self.queue_lengths
        }

    def step(self, action: Action):
        self.step_count += 1
        reward = 0.0
        reason = ""

        if action.action_type == "redirect_traffic":
            if self.queue_lengths[0] > 10:
                self.queue_lengths[0] -= 10
                self.queue_lengths[2] += 5
                reward += 0.4
                reason = "Traffic redirected"

        elif action.action_type == "open_lane":
            self.open_lanes += 1
            self.queue_lengths[0] -= 5
            reward += 0.3
            reason = "Opened new lane"

        elif action.action_type == "prioritize_emergency":
            if self.emergency_vehicle_waiting:
                self.emergency_vehicle_waiting = False
                reward += 0.8
                reason = "Emergency vehicle cleared"

        else:
            reward -= 0.1
            reason = "Invalid action"

        self.queue_lengths = [max(0, q) for q in self.queue_lengths]

        done = (
            self.step_count >= self.max_steps or
            self.queue_lengths[0] <= 10
        )

        return (
            self._get_obs(),
            Reward(score=max(0.0, min(1.0, reward)), reason=reason),
            done,
            {}
        )