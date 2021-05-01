# Tutorial 2
This tutorial introduces color histograms. In context of images, histograms can serve as feature vectors (i.e. a list of numbers used to quantify an image and compare it to other images).
  
A histogram represents the distribution of colors in an image. 
It can be visualized as a graph (or plot) that gives a high-level intuition of the intensity (pixel value) distribution. 
We are going to assume a RGB color space in this example, so these pixel values will be in the range of 0 to 255. 
If you are working in a different color space, the pixel range may be different.
    
When plotting the histogram, the X-axis serves as our “bins”. 
If we construct a histogram with 256 bins, then we are effectively counting the number of times each pixel value occurs. 
In contrast, if we use only 2 (equally spaced) bins, then we are counting the number of times a pixel is in the range [0, 128) or [128, 255]. 
The number of pixels binned to the X-axis value is then plotted on the Y-axis.
