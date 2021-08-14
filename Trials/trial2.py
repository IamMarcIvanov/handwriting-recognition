import cv2
import numpy as np
import time
import pyautogui as pag


capture = cv2.VideoCapture(1)

_, frame = capture.read()
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

lk_params = {'winSize': (20, 20),
             'maxLevel': 5,
             'criteria': (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)}


def select_point(event, x, y, flags, params):
    global point, point_selected, old_points
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        point_selected = True
        old_points = np.array([[x, y]], dtype=np.float32)


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", select_point)

point_selected = False
point = ()
old_points = np.array([[]])
while True:
    _, frame = capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if point_selected:
        # image to draw on, where to draw, radius, colour, thickness
        cv2.circle(frame, point, 5, (0, 0, 255), 2)
        
        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lk_params)
        old_gray = gray_frame.copy()
        old_points = new_points
        
        x, y = new_points.ravel()
        
        pag.hotkey('alt', 'tab')
        # pag.hotkey('alt', 'tab')
        pag.dragTo(x, y)
        
            
        cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), 2)
    
    if not point_selected:
        cv2.imshow("Frame", frame)
    
    time.sleep(0.1)
    
    key = cv2.waitKey(1)
    if key == 27:  # escape key
        break

capture.release()
cv2.destroyAllWindows()