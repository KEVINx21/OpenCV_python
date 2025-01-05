import cv2
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt.xml')

vs=cv2.VideoCapture(0)
while True:
        ret, frame=vs.read()
        if not ret:
            break
        gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces= faceCascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(25,0,0),2)

        cv2.imshow("Video",frame)

        key=cv2.waitKey(1) & 0xFF
        if key==ord("q") or key==27:
            break
vs.relese()
cv2.destroyAllWinows()
        

    

    
