import cv2

face_recognize = cv2.CascadeClassifier('haarcascade_face_without_mask.xml')                                 # Assigning XML file

cap = cv2.VideoCapture(0)                                                                                   # Capture Video 

while 1: 
    ret, img = cap.read()                                                                                   # Reading Live Video
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    face_without_mask_recognized = face_recognize.detectMultiScale(gray, 1.3, 5)                            # Detecting FaceWithoutMask

    for (x,y,w,h) in face_without_mask_recognized:
        face_without_mask = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)                                  # Marking out a rectangle on Face
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Person_Without_Wearing_Mask',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)   # Put text on Face Rectangle 

            grey_image = cv2.imread(face_without_mask,cv2.IMREAD.GREYSCALE)
            cv2.imwrite("C:\Home\ML_Project\A_Person_Without_Mask_detected",grey_image)                     # Saving Number Plates on a Folder

    cv2.imshow('img',img)                                                                                   # Showing Image
    k = cv2.waitKey(30) & 0xff                                                                              # for exit
    if k == 27:                    
        break

cap.release()
cv2.destroyAllWindows() 
