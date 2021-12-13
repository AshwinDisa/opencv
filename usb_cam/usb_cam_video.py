#!/usr/bin/env python 

import cv2

video_capture = cv2.VideoCapture(0)

while(True):
	ret, frame = video_capture.read()

	frame1 = cv2.resize(frame, (0, 0), fx=0.5,fy=0.5)
	original = cv2.imshow("Original", frame1)
	cv2.moveWindow("Original", 0, 0)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.resize(gray, (0, 0), fx = 0.5, fy = 0.5)
	gray = cv2.imshow("Grayscale", gray)
	cv2.moveWindow("Grayscale", 320, 0)


	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	hsv = cv2.resize(hsv, (0, 0), fx = 0.5, fy = 0.5)
	hsv = cv2.imshow("HSV", hsv)
	cv2.moveWindow("HSV", 320*2, 0)

	h, s, v = cv2.split(frame)
	#width = h.shape[1]
	#print "width = %s"%h.shape[1]
	h = cv2.resize(h, (0, 0), fx=0.5,fy=0.5)
	cv2.imshow("Hue", h)
	cv2.moveWindow("Hue", 0, 320)
	
	s = cv2.resize(s, (0, 0), fx=0.5,fy=0.5)
	cv2.imshow("Saturation", s)
	cv2.moveWindow("Saturation", 320, 320)
	
	v = cv2.resize(v, (0, 0), fx=0.5,fy=0.5)
	cv2.imshow("Value", v)
	cv2.moveWindow("Value", 320*2, 320)
	
	
	#cv2.line(frame,(100,100),(640,640),(255,255,255),1)
	#cv2.imshow("Frame",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
#print "img_shape = %s %s %s"%frame.shape
#print "img_size = %s"%frame.size
video_capture.release()
cv2.destroyAllWindows()
