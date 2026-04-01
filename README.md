# Car Colour Detection and Traffic Monitoring System

**Internship Extension Project**  
*Built upon Facial Emotion Detection CNN Training Project*

## Project Overview

This project develops a practical computer vision system capable of analyzing traffic scenes. It automatically detects cars, identifies their colours using a custom-trained Convolutional Neural Network (CNN), and visualizes the results with colour-coded bounding boxes. 

As per the internship requirement:
- **Blue cars** are highlighted with **Red bounding boxes**
- **All other cars** are highlighted with **Blue bounding boxes**

The system also counts the total number of cars and people in the scene. A user-friendly desktop GUI built with Tkinter enables easy image upload and result visualization.

This project demonstrates the application of deep learning concepts learned during the Emotion Detection training into a real-world use case.

## Features

- Custom CNN-based Car Colour Classification (11 classes)
- Dynamic bounding box coloring based on car colour
- Car and People counting in traffic scenes
- Clean and interactive Tkinter GUI with input/output preview
- Consistent model architecture and training pipeline with Emotion Detection project
- Easy-to-use interface suitable for demonstration

## Technologies Used

- **Python**
- **TensorFlow / Keras** (Custom CNN Model)
- **OpenCV** (Image processing and visualization)
- **NumPy**
- **Tkinter** (Graphical User Interface)

## Project Structure
```plaintext
Car_Color_Detection/
   |
   ├── car-color-detection.ipynb         # CNN Model Training Notebook
   ├── car_color_gui.py                  # Main GUI
   ├── car_color_cnn.h5                  # Pre-Trained moel
   ├── requirements.txt

```
## Installation
1. Clone the Repository
   ``` bash
   git clone https://github.com/devang06D/Car_Color_Detection_Elevance.git
   cd Car_Color_Detection_Elevance
   
 
 2. Create virtual environment
 ``` bash
   python -m venv car_env
 ```

3. Activate virtual environment (Windows)
   ``` bash
   car_env\Scripts\activate
   ```
4. Install dependencies
``` bash
    pip install -r requirements.txt
```

## How to Run
1. Ensure car_color_cnn.h5 is in the project root folder.
2. Launch the application:
  ``` bash
    python car_color_gui.py
 ```
3. Click "Select Traffic Image", choose an image, and observe the results.
