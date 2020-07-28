#Importing necessary libraries
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

#Creating trackbars for upper and lower bounds to adjust HSV parameters
cv2.namedWindow('Trackbar')
cv2.createTrackbar("LH", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("UH", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("US", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("UV", "Trackbar", 255, 255, nothing)

#Running the image loop until 'ESC' is pressed
while True:

    _,img = cap.read()

    #Converting to HSV 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Getting the lower and upper Hue trackbar positions
    l_h = cv2.getTrackbarPos("LH", "Trackbar")
    u_h = cv2.getTrackbarPos("UH", "Trackbar")
    
    #Getting the lower and upper Saturation trackbar positions
    l_s = cv2.getTrackbarPos("LS", "Trackbar")
    u_s = cv2.getTrackbarPos("US", "Trackbar")
    
    #Getting the lower and upper Value trackbar positions
    l_v = cv2.getTrackbarPos("LV", "Trackbar")
    u_v = cv2.getTrackbarPos("UV", "Trackbar")
    
    #Creating lower and upper bound HSV arrays
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    
    #Creating a mask for object detection with the HSV parameters
    mask = cv2.inRange(hsv, l_b, u_b)

    #Masking the image with the bitwise 'AND' operator
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Original', img)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()