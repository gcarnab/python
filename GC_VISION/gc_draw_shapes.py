import cv2
import numpy as np
import common.Draw as dw

def draw_shapes():
    # create a canvas from numpy array
    canvas = np.zeros((480, 480, 3), np.uint8)
    cv2.imshow("Canvas", canvas)
    print("Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # paint the canvas with a color
    canvas[:] = 235, 235, 235
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Draw a line
    dw.draw_line(canvas, start=(100,100), end=(canvas.shape[1]-100, canvas.shape[0]-100), color=(10,10,10), thickness=10 )
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Draw rectangles
    dw.draw_rectangle(canvas, (200,50), (400, 20), color=(255, 255, 0), thickness=2)
    dw.draw_rectangle(canvas, (20,220), (200, 320), color=(255, 135, 135), thickness=cv2.FILLED)

    #Draw circles
    dw.draw_circle(canvas, center=(280, 120), radius=50, color=(85, 130, 255), thickness=cv2.FILLED)
    dw.draw_circle(canvas, center=(380, 160), radius=80, color=(180, 30, 175), thickness=5)

    #Draw ellipses
    dw.draw_ellipse(canvas, center=(230,280), axes=(60,80), angle=0, start_angle=0, end_angle=360, color=(123,223,210), thickness=cv2.FILLED)

    pts = np.array([[25, 70], [25, 160],
                    [110, 200], [220, 140],
                    [200, 70], [110, 20]], np.int32)
    pts = pts.reshape((-1,1,2))
    dw.draw_polylines(canvas, [pts], color=(23,23,10))

    cv2.imshow("Canvas", canvas)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_opencv_icon(image):
    axes = (100, 100)
    center_top_circle = (320, 140)
    center_lowerleft_circle = (center_top_circle[0]-160,
                               center_top_circle[1]+240)
    center_lowerright_circle = (center_top_circle[0]+160,
                                center_top_circle[1]+240)
    angle_top_circle = 90
    angle_lowerleft_circle = -45
    angle_lowerright_circle = -90
    start_angle = 40
    end_angle = 320
    dw.draw_ellipse(image, center_top_circle, axes,
                 angle_top_circle, start_angle, end_angle,
                 color=(0, 0, 255),
                 thickness=80)
    dw.draw_ellipse(image, center_lowerleft_circle, axes,
                 angle_lowerleft_circle, start_angle, end_angle,
                 color=(0, 255, 0),
                 thickness=80)
    dw.draw_ellipse(image, center_lowerright_circle, axes,
                 angle_lowerright_circle, start_angle, end_angle,
                 color=(255, 0, 0),
                 thickness=80)
    dw.draw_text(image, "OpenCV", (20,660), color=(0,0,0),
                 font_scale=4.8, thickness=15)
    
if __name__ == '__main__':

    # create an image from numpy array
    canvas = np.zeros((480, 980, 3), np.uint8)
    canvas[:] = 235, 235, 235

    dw.draw_text(canvas, "Hello OpenCV", (150,260),
                 color=(125,0,0),
                 thickness=8, font_scale=3)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    canvas = np.zeros((720,640,3), np.uint8)
    canvas[:] = 235,235,235
    draw_opencv_icon(canvas)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
