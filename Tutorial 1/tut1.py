import cv2

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("tut1.jpg")


# d - depth represents the no. of colour channels
# image stores the dimensions as height x width 
# (corresponding to the row x column of the NumPy array)
# But when using opencv functions specify the dimensions as
# width x height as it takes care of the conversion for you
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))


# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution.
'''a call to waitKey pauses the execution of the script until we press a key on our keyboard. 
Using a parameter of “0” indicates that any keypress will un-pause the execution.'''
cv2.imshow("Image", image)
cv2.waitKey(0)


# access the RGB pixel located at x=50, y=100. Note that x is along the 
# width and y is along the height and that's why image[100,50] is used to
# access (50,100). Also note that while using opencv functions you can dirctly use
# (x,y) to provide the coordinates, the above restriction is applicable only when accessing the 
# image.  
# **OpenCV stores images in BGR order rather than RGB**
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))


# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)


# crop the image using array slices -- it's a NumPy array
# after all!
cropped = image[70:170, 440:540]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)


# saving the above image to disk
# write the cropped image to disk in PNG format
cv2.imwrite("thumbnail.png", cropped)


# resize the image to 200(width) x 200(height) px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)


# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
# here w is the original width of the image
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)


# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
# To understand this series of operations you can think of it as
# opencv using matrix multiplication to rotate the image
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0) # -45 because rotation is clockwise
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)


# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
# kernel can be simply thought as the amount of blurring you want in the image
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)


# draw a 2px thick red rectangle surrounding the face
# The values used were determined manually
# Here we have used a copy of the image to keep the original intact
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)


# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1) # a +ve value(3rd parameter) would have made an outline.
cv2.imshow("Circle", output)						# Any -ve value will fill in the outline
cv2.waitKey(0)


# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)


# draw green text on the image
output = image.copy()
# 5th param - font size
# last param - text box size
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25) ,cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
