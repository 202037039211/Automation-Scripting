# Security Camera System with Person Detection

This Python script implements a security camera system that uses YOLOv5 for person detection and records video when a person is detected in a defined region of interest (ROI). The system includes sound alerts (optional) and stores video footage when a person is detected.

## Features:
- **Real-time Camera Feed**: Captures live video feed from the webcam.
- **Person Detection**: Uses YOLOv5 to detect persons in the camera feed.
- **Region of Interest (ROI)**: Draw a polygon to define a region. The system will detect persons within this region.
- **Video Recording**: Records video whenever a person is detected.
- **Sound Alerts**: Plays a sound alert when a person is detected (optional).
  
## Requirements:
- Python 3.x
- `opencv-python` for computer vision tasks
- `torch` for YOLOv5 model inference
- `pygame` for sound alerts (optional)

## Installation:
1. Clone this repository.
2. Install required libraries:
```bash
pip install opencv-python torch pygame
```
3. Adjust the `model` loading line if needed for other YOLOv5 models or configurations.
4. Run the script with:
```bash
python main.py
```

## Usage:
1. Launch the script and draw a polygon to define the region of interest (ROI) where person detection should be active.
2. The system will start recording when a person is detected within the ROI.
3. Press 'q' to stop the script and close the camera feed.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.
