import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from ultralytics import YOLO
import os

# ========================== LOAD MODELS ==========================
model_path = 'car_color_cnn.h5'

if not os.path.exists(model_path):
    print(f"Model file '{model_path}' not found!")
    print("Please train the model first and keep 'car_color_cnn.h5' in this folder.")
    exit()

print("Loading models...")
color_model = load_model(model_path)
yolo = YOLO('yolov8n.pt')
print("Models loaded successfully!")

class_names = ['Black', 'Blue', 'Brown', 'Cyan', 'Green', 'Gray',
               'Orange', 'Red', 'Violet', 'White', 'Yellow']
BLUE_IDX = class_names.index('Blue')

# ========================== PROCESS FUNCTION ==========================
def process_and_show():
    file_path = filedialog.askopenfilename(
        title="Select Traffic Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    
    if not file_path:
        return

    # Read image
    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Could not read the image!")
        return

    # Make copy for drawing
    annotated = img.copy()
    results = yolo(img, conf=0.4)[0]

    car_count = 0
    person_count = 0

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls = int(box.cls[0])
        label = results.names[cls]

        if label == 'car':
            car_count += 1
            crop = img[y1:y2, x1:x2]
            if crop.size == 0:
                continue

            try:
                crop_resized = cv2.resize(crop, (224, 224))
                crop_array = image.img_to_array(crop_resized) / 255.0
                crop_array = np.expand_dims(crop_array, axis=0)

                pred = color_model.predict(crop_array, verbose=0)
                colour_idx = np.argmax(pred)
                colour_name = class_names[colour_idx]

                # Red box for Blue cars, Blue box for others
                box_color = (0, 0, 255) if colour_idx == BLUE_IDX else (255, 0, 0)

                cv2.rectangle(annotated, (x1, y1), (x2, y2), box_color, 3)
                cv2.putText(annotated, colour_name, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, box_color, 2)
            except:
                continue

        elif label == 'person':
            person_count += 1
            cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 255), 2)

    # Add text info
    cv2.putText(annotated, f"People: {person_count}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 3)
    cv2.putText(annotated, f"Cars: {car_count}", (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)

    # Show both images
    cv2.imshow("Input Image", img)
    cv2.imshow("Output - Car Colour Detection", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    messagebox.showinfo("Result", 
        f"Detection Complete!\n\nCars Detected: {car_count}\nPeople Detected: {person_count}")


# ========================== CREATE SIMPLE GUI ==========================
root = tk.Tk()
root.title("Car Colour Detection System")
root.geometry("700x500")
root.configure(bg="#f0f0f0")

# Title
title_label = tk.Label(root, text="Car Colour Detection", 
                       font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

desc = tk.Label(root, text="Red Rectangle = Blue Car\n\nBlue Rectangle = Other Colours\n\nYellow = People",
                font=("Arial", 11), bg="#f0f0f0", fg="#555", justify="center")
desc.pack(pady=10)

# Button
btn = ttk.Button(root, text="Select Traffic Image", command=process_and_show)
btn.pack(pady=30, ipadx=20, ipady=10)

# Info
info = tk.Label(root, text="Internship Project",
                font=("Arial", 9), bg="#f0f0f0", fg="#777")
info.pack(side="bottom", pady=30)

root.mainloop()





# -----------------------------------------------------------------------------------------------------------------
# import cv2
# import numpy as np
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from tkinter import ttk
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from ultralytics import YOLO
# import os

# # ========================== LOAD MODELS ==========================
# model_path = 'car_color_cnn.h5'

# if not os.path.exists(model_path):
#     print(f"❌ Model '{model_path}' not found!")
#     exit()

# color_model = load_model(model_path)
# yolo = YOLO('yolov8n.pt')
# print("✅ Models loaded!")

# class_names = ['Black','Blue','Brown','Cyan','Green','Gray','Orange','Red','Violet','White','Yellow']
# BLUE_IDX = class_names.index('Blue')

# # ========================== PROCESS FUNCTION ==========================
# def process_and_show():
#     file_path = filedialog.askopenfilename(
#         title="Select Traffic Image",
#         filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
#     )
#     if not file_path:
#         return

#     img = cv2.imread(file_path)
#     if img is None:
#         messagebox.showerror("Error", "Cannot read image!")
#         return

#     annotated = img.copy()
#     results = yolo(img, conf=0.4)[0]

#     car_count = 0
#     person_count = 0

#     for box in results.boxes:
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         cls = int(box.cls[0])
#         label = results.names[cls]

#         if label == 'car':
#             car_count += 1
#             crop = img[y1:y2, x1:x2]
#             if crop.size == 0: continue

#             try:
#                 crop_resized = cv2.resize(crop, (224, 224))
#                 crop_array = image.img_to_array(crop_resized) / 255.0
#                 crop_array = np.expand_dims(crop_array, axis=0)

#                 pred = color_model.predict(crop_array, verbose=0)
#                 colour_idx = np.argmax(pred)
#                 colour_name = class_names[colour_idx]

#                 box_color = (0, 0, 255) if colour_idx == BLUE_IDX else (255, 0, 0)

#                 cv2.rectangle(annotated, (x1, y1), (x2, y2), box_color, 3)

#                 # === SMALLER TEXT for car color ===
#                 font_scale = 0.5          # Smaller text
#                 thickness = 0.5
#                 (text_w, text_h), _ = cv2.getTextSize(colour_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
                
#                 cv2.rectangle(annotated, (x1, y1 - text_h - 6), (x1 + text_w + 6, y1), box_color, -1)
#                 cv2.putText(annotated, colour_name, (x1 + 3, y1 - 3), 
#                             cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), thickness)

#             except:
#                 continue

#         elif label == 'person':
#             person_count += 1
#             cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 255), 3)

#     # === SMALLER TEXT for People & Cars Count ===
#     cv2.putText(annotated, f"People: {person_count}", (20, 35),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
    
#     cv2.putText(annotated, f"Cars: {car_count}", (20, 70),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

#     # Display
#     cv2.imshow("Input Image", cv2.resize(img, (900, 600)))
#     cv2.imshow("Output - Car Colour Detection", cv2.resize(annotated, (900, 600)))
    
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     messagebox.showinfo("Summary", 
#         f"Detection Complete!\nCars: {car_count} | People: {person_count}")


# # ========================== GUI ==========================
# root = tk.Tk()
# root.title("Car Colour Detection System")
# root.geometry("700x480")
# root.configure(bg="#1e1e1e")

# tk.Label(root, text="Car Colour Detection", 
#          font=("Arial", 18, "bold"), fg="#00ffcc", bg="#1e1e1e").pack(pady=25)

# tk.Label(root, text="Red Box = Blue Car | Blue Box = Other Colours", 
#          font=("Arial", 11), fg="#ffffff", bg="#1e1e1e").pack(pady=5)

# ttk.Button(root, text="📂 Select Traffic Image", command=process_and_show).pack(pady=40, ipadx=30, ipady=12)

# tk.Label(root, text="Car Color Detection_ElevanceSkills", 
#          font=("Arial", 9), fg="#888888", bg="#1e1e1e").pack(side="bottom", pady=20)

# root.mainloop()