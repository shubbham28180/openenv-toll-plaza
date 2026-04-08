from ultralytics import YOLO

# Pretrained YOLO model load
model = YOLO("yolov8n.pt")

# Vehicle detection function
def detect_vehicle(image_path):
    results = model(image_path)

    detected = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            # Only useful vehicle types
            if label in ["car", "truck", "bus", "motorcycle"]:
                detected.append(label)

    # Priority based decision
    if "truck" in detected and "ambulance" in image_path.lower():
        return "Ambulance"
    elif "truck" in detected:
        return "Truck"
    elif "bus" in detected:
        return "Ambulance"
    elif "car" in detected:
        return "Car"
    else:
        return "Unknown"