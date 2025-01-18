import cv2
import torch
import numpy as np
import time
import datetime
# import pygame

# Initialize sound alerts (Optional, uncomment for sound)
# pygame.init()
# pygame.mixer.music.load("alert.wav")

# Load YOLOv5 model for object detection (pre-trained)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Open camera stream
cap = cv2.VideoCapture(0)

# Check if camera is accessible
if not cap.isOpened():
    print("Error: Camera not accessible.")
    exit()

# Set up video window properties
cv2.namedWindow("Camera", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

# Initialize detection-related variables
detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# List of classes to detect (person in this case)
target_classes = ['person']

# Polygon points for Region of Interest (ROI) drawing
pts = []

# Function to handle drawing polygons on the camera feed
def draw_polygon(event, x, y, flags, param):
    global pts
    if event == cv2.EVENT_LBUTTONDOWN:
        pts.append([x, y])
    elif event == cv2.EVENT_RBUTTONDOWN:
        pts = []  # Right-click to reset polygon

# Function to check if a point is inside a polygon
def inside_polygon(point, polygon):
    return cv2.pointPolygonTest(np.array([polygon]), (point[0], point[1]), False) >= 0

# Set up mouse callback for polygon drawing
cv2.setMouseCallback('Camera', draw_polygon)

# Function to preprocess the frame before passing it to YOLOv5
def preprocess_frame(img):
    height, width = img.shape[:2]
    ratio = height / width
    img = cv2.resize(img, (640, int(640 * ratio)))  # Resize to fit YOLO input
    return img

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture frame.")
        break
    
    # Get the current timestamp
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    # Display the current date and time on the frame
    cv2.putText(frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Preprocess frame for YOLOv5 detection
    frame_for_detection = preprocess_frame(frame)
    
    # Run YOLOv5 for object detection
    results = model(frame_for_detection)

    # Flag to detect if person is within the region of interest
    person_detected = False
    for index, row in results.pandas().xyxy[0].iterrows():
        center_x, center_y = None, None
        if row['name'] in target_classes:
            x1, y1 = int(row['xmin']), int(row['ymin'])
            x2, y2 = int(row['xmax']), int(row['ymax'])
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            # Draw bounding box and label for detected person
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(frame, row['name'], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # If a polygon (ROI) is defined, check if the person is inside it
            if len(pts) >= 3:
                cv2.fillPoly(frame, [np.array(pts)], (0, 255, 0))  # Draw the polygon
                if inside_polygon((center_x, center_y), pts) and row['name'] == 'person':
                    person_detected = True
                    cv2.putText(frame, "Person Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                    # Play alert sound (uncomment for sound alert)
                    # if not pygame.mixer.music.get_busy():
                    #     pygame.mixer.music.play()

                    # Start recording if person is detected
                    if not detection:
                        detection = True
                        out = cv2.VideoWriter(f"Recording_{current_time}.mp4", fourcc, 20, frame_size)
                        print("Started Recording!")
            else:
                if row['name'] == 'person':
                    person_detected = True

    # Manage recording based on detections
    if person_detected:
        if detection:
            timer_started = False
        else:
            detection = True
            out = cv2.VideoWriter(f"Recording_{current_time}.mp4", fourcc, 20, frame_size)
            # pygame.mixer.music.play()
            print("Started Recording!")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                out.release()  # Stop recording
                print("Stopped Recording!")
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)  # Write frame to video file

    # Display the live camera feed
    cv2.imshow("Camera", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources when done
if 'out' in locals():
    out.release()

cap.release()
cv2.destroyAllWindows()
