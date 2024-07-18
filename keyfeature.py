from ultralytics import YOLO
import cv2
# Load a model
model = YOLO("best.pt")

image = cv2.imread("D:\\project\\nhandienbanve\\train\\images\\image_5258_png.rf.ee5862f2e0527f7364095665d7859993.jpg") # return a list of Results objects
# Run inference on the source
results = model(image,save=True,conf = 0.3, project="runs/detect", name="inference", exist_ok=True)  # generator of Results objects
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    print(boxes)
    masks = result.masks  # Masks object for segmentation masks outputs
    names = result.names
    print(names)
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result1.jpg")  # save to disk