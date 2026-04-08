import gradio as gr
import cv2
import numpy as np
from PIL import Image
from vehicle_detector import VehicleDetector 

detector = VehicleDetector(model_path="yolov8n.pt")

def detect_cars(input_img):
    if input_img is None:
        return None, "No image uploaded"
    
    img = np.array(input_img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    result_img, count = detector.detect(img)
    
    result_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
    
    return result_img, {"vehicle_count": count, "status": "Success"}

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