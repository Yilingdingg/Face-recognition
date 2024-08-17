import cv2

face_xml="haarcascade_frontalface_default.xml"
#detect face
face_detection=cv2.CascadeClassifier(face_xml)
path="datasets/Elise"
#open camera
webcam=cv2.VideoCapture(0)
count=1
while count<31:
    ret, img=webcam.read()
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=face_detection.detectMultiScale(gray_img, 1.3, 4)
    print(face)
    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y),(x+w,y+h),(156,205,255),3)
        person=gray_img[y:y+h,x:x+h]
        person_resize=cv2.resize(person,(130,100))
        cv2.imwrite(f"{path}/{count}.png", person_resize)
    count+=1
    cv2.imshow("Webcam", img)
    key=cv2.waitKey(10)
    if key==27:
        break


