import cv2 as cv
import numpy as np
import time

CONFIDENCE = 0.5
THRESHOLD = 0.3

weights_path = "../assets/yoloface/yolov3-wider_16000.weights"
config_path = "../assets/yoloface/yolov3-face.cfg"
names_path = "../assets/yoloface/face.names"

print("Loading yoloface model...")
net = cv.dnn.readNetFromDarknet(config_path, weights_path)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)

image = cv.imread("../assets/test-person.jpg")
(h, w) = image.shape[:2]

# finds the output layer names of the YOLO model
layer_names = net.getLayerNames()
# if CUDA support -> layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
layer_names = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# construct a blob from input image and pas into inference
# acceptable sizes are 320x320, 416x416, 609x609
blob = cv.dnn.blobFromImage(image, 1 / 255.0, (320, 320),
                            swapRB=True, crop=False)
net.setInput(blob)

start = time.time()
layer_outputs = net.forward(layer_names)
end = time.time()

print("Inference took {:.6f} seconds".format(end - start))

# extract the detected faces
boxes = []
confidences = []
# class_ids = []

for output in layer_outputs:
    for detection in output:
        scores = detection[5:]

        # extracts the confidence of detecting the face (only 1 category)
        confidence = np.max(scores)

        # class_id = np.argmax(scores)
        # confidence = scores[class_id]

        if confidence > CONFIDENCE:
            # scales the output box back to the size of the image
            box = detection[0:4] * np.array([w, h, w, h])
            (center_x, center_y, width, height) = box.astype("int")

            # use the center to detect the corners of the box
            x = int(center_x - (width / 2))
            y = int(center_y - (height / 2))

            # include the box and confidence in the overall list
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            # class_ids.append(class_id)

# suppress overlapping boxes with non-maxima suppression
valid_boxes_idxs = cv.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD)
boxes = [boxes[i] for i in valid_boxes_idxs]

for (x, y, width, height) in boxes:
    cv.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)

cv.imshow("Image", image)
cv.waitKey(0)
