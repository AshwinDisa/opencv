#!/usr/bin/env python

import numpy as np
import cv2

image = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(image, (50, 50), (511-50,511-50), (255,255,255), 5)

pts = np.array([[100,100], [511-100, 100], [511-100,511-100], [100,511-100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image, [pts], True, (255,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "ROS", (100,300), font, 5, (255,255,255), 5)

cv2.imshow("Draw_image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

