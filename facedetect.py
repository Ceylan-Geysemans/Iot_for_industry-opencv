from gpiozero import LED
import cv2
import numpy as np
frameWidth = 600
frameHeight = 400

pipe = '"rtspsrc location=\"rtsp://admin:password@192.168.1.65:554/Streaming/Channels/400" latency=10 ! appsink'

led = LED(17)

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    timer = cv2.getTickCount()
    # Read the frame
    succes, img = cap.read()
    # Convert to grayscale0

    img = cv2.resize(img, (frameWidth, frameHeight))

    fps = cv2.getTickFrequency() / (cv2.getTickCount()-timer);
    cv2.putText(img,str(int(fps)),(75,110),cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2);


    Kernel = np.ones((1, 3), np.uint8)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgblur = cv2.GaussianBlur(gray, (5, 5), 0)
    imgcanny = cv2.Canny(imgblur, 100, 200)
    imgerode = cv2.erode(imgcanny, Kernel, iterations=2)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    cnt = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 3)
        cnt += 1
    cv2.putText(img, str(int(cnt)), (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 2);

    if cnt >= 1:
        print("feestje")
        led.on()
    else:
        print("njeet")
        led.off()

    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()