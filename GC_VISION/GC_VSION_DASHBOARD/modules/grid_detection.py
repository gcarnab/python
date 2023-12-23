import cv2
import matplotlib.pyplot as plt

flat_chess = cv2.imread('data/flat_chessboard.png')

plt.imshow(flat_chess,cmap='gray')

found, corners = cv2.findChessboardCorners(flat_chess,(7,7))

if found:
    print('OpenCV was able to find the corners')
else:
    print("OpenCV did not find corners. Double check your patternSize.")

print("corners.shape= " , corners.shape)

flat_chess_copy = flat_chess.copy()
result_image = cv2.drawChessboardCorners(flat_chess_copy, (7, 7), corners, found)

plt.imshow(result_image)
#print("result_image" , result_image)
"""
dots = cv2.imread('DATA/dot_grid.png')
plt.imshow(dots)

found, corners = cv2.findCirclesGrid(dots, (10,10), cv2.CALIB_CB_SYMMETRIC_GRID)

dbg_image_circles = dots.copy()
result_image = cv2.drawChessboardCorners(dbg_image_circles, (10, 10), corners, found)

plt.imshow(result_image)


"""

plt.show()