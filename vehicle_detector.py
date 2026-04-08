from ultralytics import YOLO
import cv2

class VehicleDetector:
    def __init__(self, model_path="yolov8n.pt"):
        # Load the model once when the app starts
        self.model = YOLO(model_path)

    def detect(self, frame):
        # Run YOLO on the image frame
        results = self.model(frame)
        
        detected_labels = []
        # Get the first result (since we only send one image)
        r = results[0]
        
        # This draws the boxes on the image for us!
        annotated_frame = r.plot() 

        for box in r.boxes:
            cls = int(box.cls[0])
            label = self.model.names[cls]
            if label in ["car", "truck", "bus", "motorcycle"]:
                detected_labels.append(label)

        # Logic for the count or type
        count = len(detected_labels)
        
        # Priority Logic
        if "bus" in detected_labels:
            status = "Ambulance/Bus Detected"
        elif "truck" in detected_labels:
            status = "Truck Detected"
        elif "car" in detected_labels:
            status = f"Car Detected (Total: {count})"
        else:
            status = "No Vehicles Found"

        # Return BOTH the image with boxes and the status text
        return annotated_frame, status