def suggest_lane(vehicle_type):
    if vehicle_type == "Truck":
        return "Lane 2"
    elif vehicle_type == "Car":
        return "Lane 1"
    elif vehicle_type == "Ambulance":
        return "Priority Lane"
    else:
        return "Lane 3"