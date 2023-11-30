import cv2

# Connects to your computer's default camera
cap = cv2.VideoCapture(0) #integrated default camera
#cap = cv2.VideoCapture(1) #external webcam

# Automatically grab width and height from video feed
# (returns float which we need to convert to integer for later on!)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

########## STREAMING ON A FILE ##########
# MACOS AND LINUX: *'XVID' (MacOS users may want to try VIDX as well just in case)
# WINDOWS *'VIDX'
#number_of_frames = cv2.CAP_PROP_FRAME_COUNT
number_of_frames = 25
writer = cv2.VideoWriter('GC_VISION/DATA/test.mp4', cv2.VideoWriter_fourcc(*'VIDX'),number_of_frames, (width, height))

# This loop keeps recording until you hit Q or escape the window
while True:
    
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Write the video
    writer.write(frame)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('Frame: Press Q to quit',gray) #GREY image
    cv2.imshow('Frame: Press Q to quit',frame) #grab color camera frame
    
    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release resources and destroy the windows
cap.release()
writer.release()
cv2.destroyAllWindows()