def setup_medium(env):
    env.queue_lengths = [25, 20, 18, 15]
    env.open_lanes = 3
    env.emergency_vehicle_waiting = False

def grade_medium(env):
    avg_wait = sum(env.queue_lengths) / len(env.queue_lengths)
    max_queue = max(env.queue_lengths)

    wait_score = max(0.0, 1 - avg_wait / 20)
    queue_score = max(0.0, 1 - max_queue / 30)

    return round((wait_score + queue_score) / 2, 2)