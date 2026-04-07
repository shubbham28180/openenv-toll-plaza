def setup_easy(env):
    env.queue_lengths = [30, 5, 4, 6]
    env.open_lanes = 4
    env.emergency_vehicle_waiting = False

def grade_easy(env):
    final_queue = env.queue_lengths[0]
    score = max(0.0, min(1.0, (30 - final_queue) / 20))
    return score