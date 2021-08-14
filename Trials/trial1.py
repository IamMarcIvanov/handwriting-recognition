import cv2 as cv
import imutils
import time
import sys
import numpy as np


tracker = cv.TrackerKCF_create()
video = cv.VideoCapture(r"D:\LibraryOfBabel\Projects\HandwritingRecognition\Media\hand-vid-1.mp4")
if not video.isOpened():
    print("Could not open video")
    sys.exit()

object_detector = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=40, detectShadows=False)

ret, frame = video.read()
mask = object_detector.apply(frame)
_, mask = cv.threshold(mask, 254, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

detections = []
for cnt in contours:
    area = cv.contourArea(cnt)
    if area > 100:
        x, y, w, h = cv.boundingRect(cnt)
        detections.append([x, y, w, h])
boxes_ids = tracker.update(np.asarray(detections))
for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv.putText(roi, str(id), (x, y - 15), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
cv.imshow('frame', frame)
cv.imshow('mask', mask)
cv.waitKey(30)
video.release()