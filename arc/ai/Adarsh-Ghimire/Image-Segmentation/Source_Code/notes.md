### 1. Image Classification vs. Image Segmentation vs. Object Detection

These are three fundamental tasks in computer vision, each answering a different question about an image:

* **Image Classification:**
    * **Question:** "What is in this image?"
    * **Output:** A single label describing the primary content or category of the entire image.
    * **Example:** Input: An image of a cat. Output: "Cat."

* **Object Detection:**
    * **Question:** "What objects are in this image, and where are they?"
    * **Output:** Bounding boxes around each detected object, along with a class label and a confidence score for each box.
    * **Example:** Input: An image with a cat and a dog. Output: A bounding box around the cat labeled "cat," and a bounding box around the dog labeled "dog."

* **Image Segmentation:**
    * **Question:** "Which pixels belong to which object/class?"
    * **Output:** A "mask" for each object or region of interest, coloring or outlining the exact pixel-level boundaries.
        * **Semantic Segmentation:** Groups pixels into categories (e.g., all "road" pixels, all "sky" pixels), without distinguishing individual instances of the same category.
        * **Instance Segmentation:** Identifies and delineates *each individual instance* of an object (e.g., "car 1," "car 2," "person 1," "person 2"), providing a unique mask for every single object.
    * **Example:** Input: An image with a cat and a dog. Output: A pixel-perfect outline (mask) for the cat, and a separate pixel-perfect outline (mask) for the dog. If it was semantic segmentation for "animal," it would just mark all animal pixels together.

### 2. Relation between Input Image Size and Output Size of Image Segmentation Models

For most modern image segmentation models (especially those based on U-Net or FCN architectures), the **output size (resolution) is typically the same as the input image size.**

* **How it works:** Segmentation models often downsample the input image internally (e.g., reduce resolution to extract high-level features) and then use upsampling (e.g., transposed convolutions, interpolation) to bring the feature maps back to the original input resolution. This ensures that a segmentation mask can be generated for every pixel of the original image.
* **Output Channels:** While the spatial dimensions (width x height) are the same, the output *channels* of the model usually correspond to the number of classes being segmented (e.g., if you have 10 classes, the output might be H x W x 10, where each pixel has scores for all 10 classes, and the highest score determines its class).


### 3. What are Segmentation Masks in Segmentation Task?

In the context of image segmentation, a **segmentation mask** is a pixel-level map that shows exactly where an object or area is in an image.

* **Nature:** It's essentially an image where each pixel is assigned a label or value indicating which object or semantic class it belongs to.
* **Binary Mask:** For a single object, a mask can be binary (e.g., 1 for object pixels, 0 for background pixels).
* **Multi-class/Multi-instance Mask:** For multiple objects or classes, the mask will have different pixel values corresponding to different classes or different instances of objects.
* **Purpose:**
    * To provide extremely fine-grained information about object shape and location, beyond what a simple bounding box can offer.
    * Used as the output of segmentation models, enabling tasks like pixel-accurate object counting, image editing (e.g., background removal), medical image analysis, and autonomous navigation.
* **Visualization:** Often visualized as a colored overlay on the original image, where each color represents a different object or class.




### 5. DICE Score vs. IoU Score

Both DICE Score (also known as F1-Score or Sørensen–Dice Coefficient) and IoU Score (Intersection over Union, also known as Jaccard Index) are common metrics used to measure the **overlap** between a **predicted segmentation mask** and the **ground truth mask**. They both range from 0 to 1, where 1 means perfect overlap and 0 means no overlap.

Let's imagine:
* `A` = The set of pixels in the **ground truth** (actual) mask for an object.
* `B` = The set of pixels in the **predicted** mask for the same object.

1.  **IoU Score (Intersection over Union):**
    * **Formula:** $\text{IoU} = \frac{|A \cap B|}{|A \cup B|} = \frac{\text{Area of Overlap}}{\text{Area of Union}}$
    * **Simple Idea:** It's the size of the area where both masks agree (intersection) divided by the total area covered by either mask (union).
    * **Sensitivity:** IoU tends to penalize false positives and false negatives more severely. This means if your predicted mask is slightly off, or includes extra pixels, the IoU score drops more dramatically. It's very strict about getting the boundaries right.

2.  **DICE Score (Sørensen–Dice Coefficient / F1-Score):**
    * **Formula:** $\text{DICE} = \frac{2 \times |A \cap B|}{|A| + |B|} = \frac{2 \times \text{Area of Overlap}}{\text{Sum of Areas of A and B}}$
    * **Simple Idea:** It doubles the overlap area and divides it by the sum of the areas of the two masks.
    * **Sensitivity:** DICE Score is often preferred in tasks with high class imbalance (e.g., small tumors in a large scan) because it is more sensitive to correctly identifying foreground pixels. It's slightly less strict on individual misclassifications compared to IoU, as the denominator doesn't penalize false positives/negatives quite as much as the union does.
    * **Relationship:** DICE and IoU are monotonically related, meaning if one increases, the other increases. You can convert between them: $\text{DICE} = \frac{2 \times \text{IoU}}{1 + \text{IoU}}$ and $\text{IoU} = \frac{\text{DICE}}{2 - \text{DICE}}$. DICE score is typically higher than IoU for the same amount of overlap (unless it's 0 or 1).
