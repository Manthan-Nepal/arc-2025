## Image Processing and Convolutional Neural Networks

### Image Processing
- Covered main image processing techniques like:
    - Changing color space: BGR to HSV, BGR to Gray Scale

    - Geometric transformations: Rotation, Scaling, Translation, Affine

    - Image Thresholding: Apply some value to pixel based on threshold

    - Smoothing Images: Averages pixel values, decrease noise

    - Morphological Transformation: Erosion, Dilation, Opening, Closing

    - Image Gradients: Highlights edges/regions of high intensity

    - Canny Edge Detection: Non maximum supression

    - Contours and Histograms

### CNN Models
- Worked with AlexNet, Resnet
    - Initial replication of AlexNet, from Medium webiste got metrics as follows:
        - Epochs = 10

        - Train loss: 0.1579 | Train accuracy: 0.9343

        - Val loss:   0.2190 | Val accuracy:   0.9064
    
    - Modification to AlexNet adding 2 more convolutional layers, metrics as follows:
        - Epochs = 10

        - Train loss: 0.1858 | Train accuracy: 0.9250

        - Val loss:   0.2612 | Val accuracy:   0.8966

    - Using ResNet as feature extractor, referenced from Transfer Learning resource, metrics as follows:
        - Epochs = 10

        - Train Loss: 0.0708 | Train Acc: 0.9735

        - Val Loss:   0.0549 | Val Acc:   0.9796