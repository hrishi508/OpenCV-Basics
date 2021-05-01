# Tutorial 2
This tutorial introduces color histograms. In context of images, histograms can serve as feature vectors (i.e. a list of numbers used to quantify an image and compare it to other images).
  
A histogram represents the distribution of colors in an image. 
It can be visualized as a graph (or plot) that gives a high-level intuition of the intensity (pixel value) distribution. 
We are going to assume a RGB color space in this example, so these pixel values will be in the range of 0 to 255. 
If you are working in a different color space, the pixel range may be different.  

Comparing the “similarity” of color histograms can be done using a distance metric. Common choices include: Euclidean, correlation, Chi-squared, intersection, and Bhattacharyya.  
    
When plotting the histogram, the X-axis serves as our “bins”. 
If we construct a histogram with 256 bins, then we are effectively counting the number of times each pixel value occurs. 
In contrast, if we use only 2 (equally spaced) bins, then we are counting the number of times a pixel is in the range [0, 128) or [128, 255]. 
The number of pixels binned to the X-axis value is then plotted on the Y-axis.  

We will be using the cv2.calcHist function in OpenCV to build our histograms.  
## cv2.calcHist(images, channels, mask, histSize, ranges)  
images - takes in a list of images
  
channels - [0] for greyscale, [0,1,2] for RGB  
  
mask - a mask is a uint8 image with the same shape as our original image, where pixels with a value of zero are ignored and pixels with a value greater than zero are included in the histogram computation. Can bes set as None.
  
histSize - This is the number of bins we want to use when computing a histogram. Again, this is a list, one for each channel we are computing a histogram for.
  
ranges - The range of possible pixel values. Normally, this is [0, 256] for each channel, but if you are using a color space other than RGB (such as HSV), the ranges might be different.    
