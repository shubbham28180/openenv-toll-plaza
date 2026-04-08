import gradio as gr
import cv2
import numpy as np
from PIL import Image
from vehicle_detector import VehicleDetector 

# Initialize the detector
detector = VehicleDetector(model_path="yolov8n.pt")

def detect_cars(input_img):
    if input_img is None:
        return None, "No image uploaded"
    
    # Convert PIL to OpenCV format
    img = np.array(input_img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Run detection
    result_img, count = detector.detect(img)
    
    # Convert back to RGB for Gradio
    result_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
    
    return result_img, {"vehicle_count": count, "status": "Success"}

# Create the Web Interface
demo = gr.Interface(
    fn=detect_cars,
    inputs=gr.Image(type="pil", label="Upload Toll Plaza Photo"),
    outputs=[
        gr.Image(label="Processed Image"),
        gr.JSON(label="Detection Data")
    ],
    title="OpenEnv Toll Plaza - Vehicle Detector",
    description="Upload an image to detect vehicles and manage toll lanes."
)

if __name__ == "__main__":
    demo.launch()