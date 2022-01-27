import cv2 as cv
import numpy as np
import threading

_WEIGHTS_PATH = "../assets/yoloface/yolov3-wider_16000.weights"
_CONFIG_PATH = "../assets/yoloface/yolov3-face.cfg"

_WINDOW_NAME = "portal-turret-project"

# valid blob sizes are:
# 320x320, 416x416, 609x609

# other sizes that work (experimentation)
# 128x128, 156x156, 64x64


class VideoDetector:
    def __init__(self, face_enter_callback, face_lost_callback, blob_size=156, confidence=0.5, threshold=0.3,):
        self.face_enter_callback = face_enter_callback
        self.face_lost_callback = face_lost_callback
        self.blob_size = blob_size
        self.confidence = confidence
        self.threshold = threshold

        self.face_in_view = False
        self.shutdown_issued = False

    def start(self):
        self._thr = threading.Thread(target=self._loop, args=())
        self._thr.start()

    def faceInView(self):
        return self.face_in_view

    def shutdown(self):
        self.shutdown_issued = True

    def join(self):
        self._thr.join()

    def _loop(self):
        # loads the yoloface model
        net = cv.dnn.readNetFromDarknet(_CONFIG_PATH, _WEIGHTS_PATH)
        net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)

        # identifies the output layer names
        layer_names = net.getLayerNames()
        layer_names = [layer_names[i - 1]
                       for i in net.getUnconnectedOutLayers()]

        # open a video capture
        cap = cv.VideoCapture(0)

        if (not cap.isOpened()):
            print("Failed to open the video capture")
            exit()

        while(True):
            # get the frame
            ret, frame = cap.read()

            if ret:  # if there is an image
                (frame_h, frame_w) = frame.shape[:2]

                blob = cv.dnn.blobFromImage(
                    frame, 1 / 255.0, (self.blob_size, self.blob_size), swapRB=True, crop=False)
                net.setInput(blob)

                # start = time.time()
                outputs = net.forward(layer_names)
                # end = time.time()

                # print("Inference took {:.6f} seconds".format(end - start))

                # collects the faces detected in the frame
                boxes = []
                confidences = []

                for output in outputs:
                    for detection in output:
                        # only 1 category, so can pull the confidence directly
                        confidence = detection[5]

                        if (confidence > self.confidence):
                            # scales the output box back to the size of the image
                            (box_cx, box_cy, box_w, box_h) = detection[0:4] * np.array(
                                [frame_w, frame_h, frame_w, frame_h])

                            # uses the center to detect the corners of the box
                            box_x = box_cx - box_w / 2
                            box_y = box_cy - box_h / 2

                            # include the box and confidence in the overall list
                            boxes.append(
                                np.array([box_x, box_y, box_w, box_h], dtype=int))
                            confidences.append(float(confidence))

                # filters out the overlapping boxes
                valid_boxes = [boxes[i] for i in cv.dnn.NMSBoxes(
                    boxes, confidences, self.confidence, self.threshold)]

                # draws the boxes onto the images
                for (x, y, w, h) in valid_boxes:
                    cv.rectangle(frame, (x, y), (x + w, y + h),
                                 (255, 127, 0), 2)

                # display the frame
                cv.imshow(_WINDOW_NAME, frame)

                # press ESC to exit
                if (cv.waitKey(25) & 0xFF == 27 or self.shutdown_issued):
                    break

                # handles the event callbacks
                if (len(valid_boxes) > 0 and not self.face_in_view):
                    self.face_enter_callback()
                    self.face_in_view = True
                elif (len(valid_boxes) == 0 and self.face_in_view):
                    self.face_lost_callback()
                    self.face_in_view = False

            else:  # if there isn't an image
                break

        cap.release()
