import cv2
import numpy as np
from ultralytics import YOLO
from sort.sort import Sort  # Assuming sort.py is in the same directory

# 1. Load YOLOv8 model
model = YOLO("/content/yolo11n.pt")
# 2. Initialize SORT tracker
# max_age: Number of consecutive frames an unmatched track is kept. Higher = more persistence.
# min_hits: Minimum number of detections required to establish a track.
# iou_threshold: Minimum IoU for a detection to be associated with a track.
mot_tracker = Sort(max_age=30, min_hits=3, iou_threshold=0.3)

# 3. Load video
video_path = "/content/roboflow_annotation.mp4"
cap = cv2.VideoCapture(video_path)

# Prepare output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Codec for .mp4
out = cv2.VideoWriter('output_sort_tracking.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS),
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    print(f"Processing frame {frame_count}...")

    # Perform detection with YOLOv8
    # Added device='cpu' to prevent CUDA errors if GPU is busy or unavailable
    results = model(frame, verbose=False)[0] # Run inference, get the first result object

    # Extract detections in the format SORT expects: [x1, y1, x2, y2, confidence]
    detections = []
    if results.boxes.data is not None:
        # results.boxes.data contains [x1, y1, x2, y2, confidence, class_id]
        for *xyxy, conf, cls in results.boxes.data:
            # Filter by confidence if desired
            if conf > 0.5: # Example confidence threshold
                detections.append([xyxy[0].item(), xyxy[1].item(), xyxy[2].item(), xyxy[3].item(), conf.item()])

    # Convert to numpy array if detections exist, otherwise an empty array
    detections = np.array(detections) if detections else np.empty((0, 5))

    # Update SORT tracker
    # The `update` method takes detections and returns tracked objects
    # Each tracked object is [x1, y1, x2, y2, object_id]
    tracks = mot_tracker.update(detections)

    # Visualize results
    for track in tracks:
        x1, y1, x2, y2, track_id = map(int, track)

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) # Green box

        # Draw ID
        text = f"ID: {track_id}"
        cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Write the frame to the output video
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()
print("SORT tracking complete. Output saved to output_sort_tracking.mp4")
