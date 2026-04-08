# Toll Plaza Operations Environment

This project simulates an AI-based smart toll plaza system.

## Features
- Vehicle Number Plate Recognition using EasyOCR
- FASTag Verification
- Automatic Vehicle Detection using YOLOv8
- Detects Car, Truck, Ambulance and Fire Truck
- Emergency Vehicle Priority Lane
- Automatic Lane Suggestion
- Traffic Management for Easy, Medium and Hard scenarios

## Vehicle Flow
1. Read vehicle image
2. Detect number plate
3. Check FASTag status
4. Detect vehicle type automatically
5. Suggest best lane
6. Give priority lane to emergency vehicles

## Project Files
- `inference.py` → Main project file
- `vehicle_detector.py` → Vehicle detection logic
- `fastag.py` → FASTag verification
- `lane.py` → Lane suggestion logic

## Run Project
```bash
pip install -r requirements.txt
python inference.py