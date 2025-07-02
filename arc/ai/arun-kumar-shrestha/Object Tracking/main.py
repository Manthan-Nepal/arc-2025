import os
import random

import cv2
from ultralytics import YOLO

from tracker import Tracker


video_path = os.path.join('.', 'room.mp4')
video_out_path = os.path.join('.', 'out.mp4')

cap = cv2.VideoCapture(video_path)
# Get rotation metadata (if available)
rotation = 0
try:
    # Check for OpenCV's orientation metadata property
    if cv2.__version__ >= "3.4.0":  # Property available in OpenCV 3.4+
        rotation_flag = cv2.CAP_PROP_ORIENTATION_META
    else:
        rotation_flag = 6  # Fallback for older versions

    rotation = cap.get(rotation_flag)
except:
    rotation = 0

# Read first frame to get dimensions
ret, frame = cap.read()
if not ret:
    exit()

# Apply rotation correction to the frame
if rotation == 90:
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
elif rotation == 270:
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
elif rotation == 180:
    frame = cv2.rotate(frame, cv2.ROTATE_180)

# Set output dimensions (may swap width/height if rotated)
out_width = frame.shape[1]
out_height = frame.shape[0]

cap_out = cv2.VideoWriter(video_out_path, cv2.VideoWriter_fourcc(*'MP4V'),
                          cap.get(cv2.CAP_PROP_FPS), (out_width, out_height))

model = YOLO("./best.pt")
tracker = Tracker()

colors = [(random.randint(0, 255), random.randint(0, 255),
           random.randint(0, 255)) for j in range(10)]

detection_threshold = 0
while ret:

    # Apply rotation to each frame
    if rotation == 90:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif rotation == 270:
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif rotation == 180:
        frame = cv2.rotate(frame, cv2.ROTATE_180)

    results = model(frame)

    for result in results:
        detections = []
        for r in result.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = r
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            class_id = int(class_id)
            if score > detection_threshold:
                detections.append([x1, y1, x2, y2, score])

        tracker.update(frame, detections)

        for track in tracker.tracks:
            bbox = track.bbox
            x1, y1, x2, y2 = bbox
            track_id = track.track_id

            cv2.rectangle(frame, (int(x1), int(y1)), (int(
                x2), int(y2)), (colors[track_id % len(colors)]), 3)

            # cv2.imshow('fjdosi', frame)
            # cv2.waitKey(0)

    cap_out.write(frame)
    ret, frame = cap.read()

cap.release()
cap_out.release()
cv2.destroyAllWindows()
