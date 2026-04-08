# OpenEnv: Toll Plaza Simulation
A real-world simulation of an automated toll booth management system.

## Action Space
- `collect_20`: Collects the standard truck toll.
- `open_gate`: Opens the physical barrier for the vehicle.

## Observation Space
- `view`: String description of the vehicle at the gate (detected via YOLO).
- `metadata`: Contains the `task_id`.

## Tasks
1. **Easy**: Standard Sedan needs gate access.
2. **Medium**: Heavy truck requires toll collection before opening gate.
3. **Hard**: Emergency Ambulance requires immediate free passage.