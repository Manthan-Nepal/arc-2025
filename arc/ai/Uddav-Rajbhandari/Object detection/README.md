# Topics
1. Object Detection
# Objectives
1. To learn different object detection algorithms


# Tasks
1. What is Non-Max Suppression (NMS) and how does it work?
2. What are the evaluation metrics used for object detection tasks? Is there any relationship between those metrics and IoU?
3. Download and study the format of following datasets. Try to visualize the image and bounding boxes.
- [Pascal VOC](https://www.kaggle.com/datasets/gopalbhattrai/pascal-voc-2012-dataset)
- [COCO Dataset](https://www.kaggle.com/datasets/awsaf49/coco-2017-dataset) [Very Large dataset so, only download only few files to study]
4. Record a 1-minute video of your surrounding from your mobile. Make sure it captures distinct surrounding objects. Define at least 3 different classes of objects that you would like to detect such as ball, fan, clock. Then, annotate that data using [roboflow](https://roboflow.com/annotate). Export the dataset into different formats like YOLO, COCO and PASCAL.
5. Using the custom prepared dataset in task 4, train model:
- [yolov8n from ultralytics](https://docs.ultralytics.com/tasks/detect/)
6. [Finetune Mask-RCNN for object detection](https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial.html)