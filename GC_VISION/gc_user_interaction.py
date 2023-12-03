import numpy as np
import cv2
import common.Draw as dw
import math

#====== VARIABLES ======#
drawing = False
final_color = (255, 255, 255)
drawing_color = (255, 255, 0)
pt_first = (0, 0)
pt_second = (0, 0)
pts = []

#
# List all events support by cv2
#
def list_event():
    for event in dir(cv2):
        if "EVENT" in event:
            print(event)

#
# Display coordinates and color RGB value on a separate window
# when mouse clicked on the image
#
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        mycolorImage = np.zeros((100, 280, 3), np.uint8)
        mycolorImage[:] = [blue, green, red]
        strBGR = "(B,G,R) = (" + str(blue) + ", " + str(green) + ", " + str(red) + ")"
        strXY = "(X,Y) = (" + str(x) + ", " + str(y) + ")"
        txtFont = cv2.FONT_HERSHEY_COMPLEX
        txtColor = (255, 255, 255)
        cv2.putText(mycolorImage, strXY, (10, 30), txtFont, .6, txtColor, 1)
        cv2.putText(mycolorImage, strBGR, (10, 50), txtFont, .6, txtColor, 1)
        cv2.imshow("color", mycolorImage)

def main01_color():
    global img
    img = cv2.imread("GC_VISION/DATA/gc_full_image.jpg")
    list_event()
    cv2.imshow("image", img)
    cv2.setMouseCallback("image", mouse_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#============================================================#

def on_mouse_crop(event, x, y, flags, param):
    global pt_first, pt_second, drawing, img, img_bk, img_original
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt_first = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = img_bk.copy()
            draw_rectangle(img, pt_first, (x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        pt_second = (x, y)
        draw_rectangle(img, pt_first, pt_second, True)
        crop_image(img_original, pt_first, pt_second)

def crop_image(img, pt_first, pt_second):
    x_tl, y_tl = pt_first               # top-left point
    x_br, y_br = pt_second              # bottom-right point
    if x_br < x_tl:                     # swap x value if opposite
        x_br, x_tl = x_tl, x_br
    if y_br < y_tl:                     # swap y value if opposite
        y_br, y_tl = y_tl, y_br
    cropped_image = img[y_tl:y_br, x_tl:x_br]
    cv2.imshow("Cropped Image", cropped_image)

def draw_rectangle(img, point1, point2, is_final=False):
    if is_final == False:
        dw.draw_rectangle(img, point1, point2, drawing_color)
        dw.draw_text(img, str(point1), point1, color=drawing_color, font_scale=0.5)
        dw.draw_text(img, str(point2), point2, color=final_color, font_scale=0.5)
    else:
        dw.draw_rectangle(img, point1, point2, final_color, thickness=2)
        dw.draw_text(img, str(point1), point1, color=final_color, font_scale=0.5)
        dw.draw_text(img, str(point2), point2, color=final_color, font_scale=0.5)

def print_instruction(img):
    txtInstruction = "Press left button to drag a rectangle, release it to crop. ESC to exit."
    dw.draw_text(img,txtInstruction, (10, 20), 0.5, (0, 0, 0))
    print(txtInstruction)


def main02_crop():
    global img, img_bk, img_original
    windowName = 'Crop an Image'
    img = cv2.imread("GC_VISION/DATA/gc_full_image.jpg")
    img_original = img.copy()
    print_instruction(img)
    img_bk = img.copy()
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName, on_mouse_crop)
    while (True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()

#===============================================================#

def on_mouse_circle(event, x, y, flags, param):
    global drawing, ctr, radius, img, img_bk
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ctr = x, y
        radius = 0
        draw_circle(img, ctr, radius, drawing_color)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = img_bk.copy()
            radius = calc_radius(ctr, (x,y))
            draw_circle(img, ctr, radius, drawing_color)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        radius = calc_radius(ctr, (x,y))
        draw_circle(img, ctr, radius, final_color, 2, True)
        img_bk = img.copy()

def calc_radius(center, current_point):
    cx, cy = current_point
    tx, ty = center
    return int(math.hypot(cx - tx, cy - ty))

def draw_circle(img, center, r, color, line_scale=1, is_final=False ):
    txtCenter = "ctr=(%d,%d)" % center
    txtRadius = "r=%d" % radius
    if is_final == True:
        print("Completing circle with %s and %s" % (txtCenter, txtRadius))
    dw.draw_circle(img, center, 1, color, line_scale)   # draw center point
    dw.draw_circle(img, center, r, color, line_scale)   # draw circle
    dw.draw_text(img, txtCenter, (center[0]-60, center[1]+20), 0.5, color)
    dw.draw_text(img, txtRadius, (center[0]-15, center[1]+35), 0.5, color)

def main03_circle():
    global img, img_bk
    windowName = 'Mouse Drawing Circles'
    img = np.zeros((500, 640, 3), np.uint8)
    print_instruction(img)
    img_bk = img.copy()
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName, on_mouse_circle)
    while (True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()

#===============================================================#

def on_mouse_poly(event, x, y, flags, param):
    global pts, drawing, img, img_bk
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        add_point(pts, (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = img_bk.copy()
            draw_polygon(img, pts, (x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        add_point(pts, (x, y), True)
        draw_polygon(img, pts, (x, y), True)
        drawing = False
        pts.clear()
        img_bk = img.copy()

def add_point(points, curt_pt, is_final=False):
    print("Adding point #%d with position(%d,%d)"
          % (len(points), curt_pt[0], curt_pt[1]))
    points.append(curt_pt)
    if is_final == True:
        print("Completing polygon with %d points." % len(pts))

def draw_polygon(img, points, curt_pt, is_final=False):
    if (len(points) > 0):
        if is_final == False:
            dw.draw_polylines(img, np.array([points]), False, final_color)
            dw.draw_line(img, points[-1], curt_pt, drawing_color)
        else:
            dw.draw_polylines(img, np.array([points]), True, final_color)
        for point in points:
            dw.draw_circle(img, point, 2, final_color, 2)
            dw.draw_text(img, str(point), point, color=final_color, font_scale=0.5)

def main04_poly():
    global img, img_bk
    windowName = 'Mouse Drawing Polygon'
    img = np.zeros((500, 640, 3), np.uint8)
    print_instruction(img)
    img_bk = img.copy()
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName, on_mouse_poly)
    while (True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()

#===============================================================#

def on_trackbar(val):
    print("Trackbar value:", val)

def main05_trackbar(): 
    cv2.namedWindow("Trackbar Window")
    cv2.createTrackbar("Trackbar", "Trackbar Window", 0, 100, on_trackbar)
    canvas = np.zeros((100, 800, 3), np.uint8)
    canvas[:] = 235,235,235

    while True:
        cv2.imshow("Trackbar Window", canvas)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

#===============================================================#

def change_brightness(value):
    global cap
    print("Brightness: " + str(value))
    cap.set(cv2.CAP_PROP_BRIGHTNESS, value)

def change_contrast(value):
    print("Contrast: " + str(value))
    cap.set(cv2.CAP_PROP_CONTRAST, value)

def change_saturation(value):
    print("Saturation: " + str(value))
    cap.set(cv2.CAP_PROP_SATURATION, value)

def change_hue(value):
    print("Hue: " + str(value))
    cap.set(cv2.CAP_PROP_HUE, value)

def resize(image, percent):
    width = int(image.shape[1] * percent / 100)
    height = int(image.shape[0] * percent / 100)
    resized_image = cv2.resize(image, (width, height))
    return resized_image


def main06_user_track():
    global cap
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)      # set width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)     # set height
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 100)       # set initial brightness
    cap.set(cv2.CAP_PROP_CONTRAST, 50)          # set initial contrast
    cap.set(cv2.CAP_PROP_SATURATION, 90)        # set initial saturation
    cap.set(cv2.CAP_PROP_HUE, 15)               # set initial hue

    cv2.namedWindow('Webcam')
    cv2.createTrackbar('Brightness', 'Webcam', 100,300, change_brightness)
    cv2.createTrackbar('Contrast', 'Webcam', 50, 300, change_contrast)
    cv2.createTrackbar('Saturation', 'Webcam', 90, 100, change_saturation)
    cv2.createTrackbar('Hue', 'Webcam', 15, 360, change_hue)

    success, img = cap.read()
    while success:
        cv2.imshow("Webcam", resize(img, 90))

        # Press ESC key to break the loop
        if cv2.waitKey(10) & 0xFF == 27:
            break
        success, img = cap.read()

    cap.release()
    cv2.destroyWindow("Webcam")


if __name__ == '__main__':
    main01_color()
    #main02_crop()
    #main03_circle()
    #main04_poly()
    #main05_trackbar()
    #main06_user_track()