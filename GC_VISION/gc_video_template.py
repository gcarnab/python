import cv2

# Connects to your computer's default camera
cap = cv2.VideoCapture(0) #integrated default camera


# Automatically grab width and height from video feed
# (returns float which we need to convert to integer for later on!)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# This loop keeps recording until you hit Q or escape the window
while True:
    
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Frame: Press Q to quit',frame) #grab color camera frame
    
    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release resources and destroy the windows
cap.release()

cv2.destroyAllWindows()