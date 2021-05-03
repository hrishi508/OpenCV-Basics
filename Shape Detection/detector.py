import numpy as np
import cv2
import imutils

img = cv2.imread('shapes.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)


cv2.imshow('img',thresh)
cv2.waitKey(0)

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)


for cnt in contours:

    approx = cv2.approxPolyDP(cnt, .03 * cv2.arcLength(cnt, True), True)
    print len(approx)

    if len(approx)==3:
        print "triangle"
        cv2.drawContours(img,[cnt],0,(122,212,78),-1)

    elif len(approx)==4:
        print "square"
        cv2.drawContours(img,[cnt],0,(94,234,255),-1)

    elif len(approx)==8:
        area = cv2.contourArea(cnt)
        (cx, cy), radius = cv2.minEnclosingCircle(cnt)
        circleArea = radius * radius * np.pi

        a = area
        b = circleArea
        eps = 1e-10
        # compute the chi-squared distance
        d = 0.5 * ((a - b) ** 2) / (a + b + eps)
        
        if d < 0.5:
            print "circle"
            cv2.drawContours(img, [cnt], 0, (220, 152, 91), -1)

    cv2.imshow('img',img)
    cv2.waitKey(0)


cv2.imshow('img',img)
cv2.waitKey(0)

