import cv2
import time

# Same command function as streaming, its just now we pass in the file path, nice!
cap = cv2.VideoCapture('GC_VISION/DATA/hand_move.mp4')

# FRAMES PER SECOND FOR VIDEO
fps = 25

# check if the video was acutally there
if cap.isOpened()== False: 
    print("Error opening the video file.")
    

# While the video is opened
while cap.isOpened():
    
    # Read the video file.
    ret, frame = cap.read()
    
    # If we got frames, show them.
    if ret == True:
        # Display the frame at same frame rate of recording
        time.sleep(0/fps) # reduce video speed
        cv2.imshow('Frame : Press Q to quit',frame)
 
        # Press q to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):   
            break
 
    # Or automatically break this whole loop if the video is over.
    else:
        break

# When everything done, release resources and destroy the windows        
cap.release()
cv2.destroyAllWindows()