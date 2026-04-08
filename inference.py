from environment import TollPlazaEnv
from models import Action
from tasks.easy_task import setup_easy
from tasks.medium_task import setup_medium
from tasks.hard_task import setup_hard
from tasks.graders import get_score
from fastag import check_fastag
from lane import suggest_lane

import cv2
import easyocr

# OCR reader for number plate recognition
reader = easyocr.Reader(['en'])

tasks = ["easy", "medium", "hard"]

for task in tasks:
    env = TollPlazaEnv()
    env.reset()

    if task == "easy":
        setup_easy(env)

    elif task == "medium":
        setup_medium(env)

    elif task == "hard":
        setup_hard(env)

    print(f"[START] task={task}")

    done = False

    while not done:
        if env.emergency_vehicle_waiting:
            action = Action(action_type="prioritize_emergency")

        elif env.queue_lengths[0] > 15:
            action = Action(action_type="redirect_traffic")

        else:
            action = Action(action_type="open_lane")

        obs, reward, done, info = env.step(action)

        # Number Plate Recognition
        image = cv2.imread("vehicle.jpg")

        if image is not None:
            plate_image = image[100:180, 150:350]
            result = reader.readtext(plate_image)

            for r in result:
                vehicle_number = r[1]
                print(f"Vehicle Number: {vehicle_number}")
                status = check_fastag(vehicle_number)
                print(f"FASTag Status: {status}")
                from vehicle_detector import detect_vehicle

                image_path = "ambulance.jpg.jpeg"
                vehicle_type = detect_vehicle(image_path)

                emergency_vehicles = ["Ambulance", "Fire Truck", "Police Car"]

                if vehicle_type in emergency_vehicles:
                    print("🚨 Emergency Vehicle Detected!")
                    lane = "PRIORITY LANE"
                else:
                    lane = suggest_lane(vehicle_type)

            print(f"Vehicle Type: {vehicle_type}")
            print(f"Suggested Lane: {lane}")

        print(
            f"[STEP] step={obs.step_number} "
            f"action={action.action_type} "
            f"reward={reward.score}"
        )

    score = get_score(task, env)

    print(f"[END] task={task} score={score}")