import picamera
import cv2
import time

camera = picamera.PiCamera()
camera.start_preview()
time.sleep(5)
camera.capture('snapshot.jpg')
camera.stop_preview()

#Load an image from file
image = cv2.imread("/home/pi/snapshot.jpg", 3)

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Convert to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print "Found "+str(len(faces))+" face(s)"

#Draw a rectangle around every found face
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

#Save the result image
cv2.imwrite('result1.jpg',image)
