# Car Colour Detection and Traffic Monitoring System

## Project Overview
This project is a computer vision based traffic analysis system that detects vehicles and people from traffic images and identifies the colour of detected cars. The system uses a pretrained YOLOv8 object detection model to locate cars and pedestrians in the image. After detecting a vehicle, the system analyzes the cropped car region to estimate its colour.

According to the project requirement, the bounding box colour changes depending on the detected car colour:

- Blue cars are highlighted with a **red bounding box**
- Cars of any other colour are highlighted with a **blue bounding box**

Additionally, the system counts the number of people detected in the traffic scene and displays it on the screen.

A graphical user interface (GUI) built using **Tkinter** allows the user to upload traffic images and visualize the detection results interactively.

---

## Features
- Vehicle detection using **YOLOv8**
- Car colour identification
- Dynamic bounding box colouring based on detected colour
- Pedestrian detection and counting
- Interactive GUI for uploading and previewing images
- Real-time visualization of detection results

---

## Technologies Used
- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- NumPy  
- Tkinter (GUI)  
- Pillow  
- PyTorch  

---

## System Workflow

```
Input Traffic Image
        ↓
YOLOv8 Object Detection
        ↓
Detect Cars and People
        ↓
Crop Car Region
        ↓
Car Colour Detection
        ↓
Apply Bounding Box Rule
        ↓
Display Results in GUI
```

---

## Project Structure

```
carColor/
│
├── dataset/            # Sample traffic images
├── model/
│   └── yolov8s.pt      # Pretrained YOLO model
│
├── gui.py              # GUI application
├── detector.py         # Vehicle and person detection
├── color_detector.py   # Car colour detection logic
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/devang06D/Car_Color_Detection_Elevance.git
cd car-colour-detection
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate virtual environment

Windows:
```
venv\Scripts\activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

## Run the Project

```
python gui.py
```

### Steps
1. Click **Upload Image**
2. Select a traffic image
3. Click **Detect Cars**
4. View the detection results in the GUI preview

---

## Example Output

The system detects vehicles and applies bounding boxes based on detected colour:

- Blue car → **Red bounding box**
- Other coloured cars → **Blue bounding box**
- Displays **total number of people** detected in the scene

---

## Learning Outcomes

Through this project I learned:

- Implementing object detection using YOLOv8
- Integrating computer vision models with GUI applications
- Image preprocessing and region-based analysis
- Working with pretrained deep learning models
- Building end-to-end computer vision applications in Python

---

## Future Improvements
- Real-time video based traffic monitoring
- Improved car colour classification using a trained deep learning model
- Vehicle tracking and traffic flow analysis
- Integration with smart traffic management systems
