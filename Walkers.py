import cv2


# Create our body classifier
classifier = cv2.CascadeClassifier("C:/Users/This PC/Desktop/Python/PRO-106-ProjectTemplate-main/haarcascade_fullbody.xml")


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    body = classifier.detectMultiScale(grey,1.2,3)

    for x,y,w,h in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("Bodies",frame)
    #Convert Each Frame into Grayscale

    if cv2.waitKey(25) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
