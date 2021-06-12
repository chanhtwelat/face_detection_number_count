#import opencv liberia
import cv2

#Create new cam
cap = cv2.VideoCapture(1)

# initialize the face recognizer (default face haar cascade)
face_cascade = cv2.CascadeClassifier("/home/pi/OpenCV_Python/haarcascade_frontalface_default.xml")


while True:
    # Read image from webcam
    success, image = cap.read()
    
    #Converting image to gray
    imgGRAY = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(imgGRAY,1.3,5)
    
    if len(faces) == 0:
        print('No Faces Found')
        
    else:
        print(faces.shape)
        print("Number of faces detected: " + str(faces.shape[0]))
        for x,y,w,h in faces:
           cv2.rectangle(image, (x,y), (x+w, y+h), color=(255,0,0), thickness=3)
        cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
        cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

    cv2.imshow('output', image)
    if cv2.waitKey(1) == ord ('q'):
        break
cap.release()
cv2.destroyAllWindows()