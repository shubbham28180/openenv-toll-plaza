def setup_hard(env):
    env.queue_lengths = [35, 30, 25, 20]
    env.open_lanes = 3
    env.emergency_vehicle_waiting = True

def grade_hard(env):
    ambulance_score = 1.0 if not env.emergency_vehicle_waiting else 0.0
    avg_wait = sum(env.queue_lengths) / len(env.queue_lengths)
    traffic_score = max(0.0, 1 - avg_wait / 30)

    return round(0.7 * ambulance_score + 0.3 * traffic_score, 2)