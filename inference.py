from environment import TollPlazaEnv
from models import Action
from tasks.easy_task import setup_easy
from tasks.medium_task import setup_medium
from tasks.hard_task import setup_hard
from tasks.graders import get_score
from fastag import check_fastag
from lane import suggest_lane
from vehicle_detector import VehicleDetector # Changed to Class import

import cv2
import easyocr

# 1. Initialize tools ONCE at the top
reader = easyocr.Reader(['en'])
detector = VehicleDetector(model_path="yolov8n.pt") 

tasks = ["easy", "medium", "hard"]

for task in tasks:
    env = TollPlazaEnv()
    obs, info = env.reset() # Reset returns two values

    if task == "easy":
        setup_easy(env)
    elif task == "medium":
        setup_medium(env)
    elif task == "hard":
        setup_hard(env)

    print(f"--- [START] task={task} ---")
    done = False

    while not done:
        # Decision Logic
        if env.emergency_vehicle_waiting:
            action = Action(action_type="prioritize_emergency")
        elif env.queue_lengths[0] > 15:
            action = Action(action_type="redirect_traffic")
        else:
            action = Action(action_type="open_lane")

        # 2. Updated return values for OpenEnv/Gymnasium
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        # Number Plate Recognition
        image = cv2.imread("vehicle.jpg")
        if image is not None:
            # Simple crop for plate
            plate_image = image[100:180, 150:350]
            result = reader.readtext(plate_image)

            for r in result:
                vehicle_number = r[1]
                status = check_fastag(vehicle_number)
                
                # 3. Use the Class-based detector we built
                # We pass the image, it returns the annotated frame and the label
                annotated_img, vehicle_type = detector.detect(image)

                emergency_vehicles = ["Ambulance", "Fire Truck", "Police Car"]
                if "Ambulance" in vehicle_type or "Fire Truck" in vehicle_type:
                    lane = "PRIORITY LANE"
                else:
                    lane = suggest_lane(vehicle_type)

                print(f"Vehicle: {vehicle_number} | Type: {vehicle_type} | Lane: {lane}")

        print(f"[STEP] action={action.action_type} reward={reward}")

    score = get_score(task, env)
    print(f"[END] task={task} score={score}")