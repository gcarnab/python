import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chess = cv2.imread('DATA/flat_chessboard.png')
flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
#plt.imshow(flat_chess)

gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
#plt.imshow(gray_flat_chess,cmap='gray')

real_chess = cv2.imread('DATA/real_chessboard.jpg')
real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)

gray_real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)
#plt.imshow(gray_real_chess,cmap='gray')


# Convert Gray Scale Image to Float Values
gray = np.float32(gray_flat_chess)

####### Corner Harris Detection ######
dst = cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)

# result is dilated for marking the corners, not important to actual corner detection
# this is just so we can plot out the points on the image shown
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
flat_chess[dst>0.01*dst.max()]=[255,0,0]

plt.imshow(flat_chess)

# Convert Gray Scale Image to Float Values
gray = np.float32(gray_real_chess)

# Corner Harris Detection
dst = cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)

# result is dilated for marking the corners, not important to actual corner detection
# this is just so we can plot out the points on the image shown
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
real_chess[dst>0.01*dst.max()]=[255,0,0]

plt.imshow(real_chess)

# Need to reset the images since we drew on them
flat_chess = cv2.imread('DATA/flat_chessboard.png')
flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
real_chess = cv2.imread('DATA/real_chessboard.jpg')
real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
gray_real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)

####### Shi-Tomasi Detection ######
corners = cv2.goodFeaturesToTrack(gray_flat_chess,64,0.01,10)
corners = np.intp(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(flat_chess,(x,y),5,(255, 255, 0),-1)

plt.imshow(flat_chess)


corners = cv2.goodFeaturesToTrack(gray_real_chess,80,0.01,10)
corners = np.intp(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(real_chess,(x,y),5,(255, 255, 0),-1)

#plt.imshow(real_chess)

"""
# Plot Images
plt.subplot(151)
plt.imshow(flat_chess)
plt.title('Image 1')

plt.subplot(152)
plt.imshow(gray_flat_chess)
plt.title('Image 2')

plt.subplot(153)
plt.imshow(real_chess)
plt.title('Image 3')  

plt.subplot(154)
plt.imshow(gray_real_chess)
plt.title('Image 4')  

plt.subplot(155)
plt.imshow(real_chess)
plt.title('Image 5')  

"""

plt.show()