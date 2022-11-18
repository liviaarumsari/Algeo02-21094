# import the opencv library
import cv2
import time

def openWebcam():
    start = time.time()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # define a video capture object
    vid = cv2.VideoCapture(0)
    delta = 0
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
        
        for(x,y,w,h) in faces:
            # roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            img_item = "src/my-face.png"
            cv2.imwrite(img_item,roi_color)
            color = (255,0,0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
        endTime = time.time()

        # # Display the resulting frame
        cv2.imshow('frame', frame)
        if(endTime - start >= 10):
            break
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()