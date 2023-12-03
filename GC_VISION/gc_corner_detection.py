import cv2 
import numpy as np  

import matplotlib.pyplot as plt

flat_chess = cv2.imread('GC_VISION/DATA/flat_chessboard.png')
flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
#plt.imshow(flat_chess)

gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
#plt.imshow(gray_flat_chess,cmap='gray')

real_chess = cv2.imread('GC_VISION/DATA/real_chessboard.jpg')
real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
#plt.imshow(real_chess)

#===== Harris Corner Detection =====#

gray_real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)
#plt.imshow(gray_real_chess,cmap='gray')

# Convert Gray Scale Image to Float Values
gray = np.float32(gray_flat_chess)

# Corner Harris Detection
dst = cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)

# result is dilated for marking the corners, not important to actual corner detection
# this is just so we can plot out the points on the image shown
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
flat_chess[dst>0.01*dst.max()]=[255,0,0]

#plt.imshow(flat_chess)

#===== Real chess board Corner Detection =====#

# Convert Gray Scale Image to Float Values
gray = np.float32(gray_real_chess)

# Corner Harris Detection
dst = cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)

# result is dilated for marking the corners, not important to actual corner detection
# this is just so we can plot out the points on the image shown
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
real_chess[dst>0.01*dst.max()]=[255,255,0]

#plt.imshow(real_chess)

#==== Shi-Tomasi Corner Detector ====#
"""
goodFeatureToTrack Function Parameters

* image Input 8-bit or floating-point 32-bit, single-channel image.
* corners Output vector of detected corners.
* maxCorners Maximum number of corners to return. If there are more corners than are found,
* the strongest of them is returned. `maxCorners <= 0` implies that no limit on the maximum 
* is set and all detected corners are returned.
* qualityLevel Parameter characterizing the minimal accepted quality of image corners. 
* The parameter value is multiplied by the best corner quality measure, which is the minimal 
* eigenvalue (see #cornerMinEigenVal ) or the Harris function response (see #cornerHarris ). 
* The corners with the quality measure less than the product are rejected. 
* For example, if the best corner has the quality measure = 1500, and the qualityLevel=0.01 , 
* then all the corners with the quality measure less than 15 are rejected.
"""
corners = cv2.goodFeaturesToTrack(gray_real_chess,64,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(real_chess,(x,y),3,(255,255,0),-1)

plt.imshow(real_chess)


plt.show()