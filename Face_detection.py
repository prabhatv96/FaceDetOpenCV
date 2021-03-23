import cv2

face_cascade = cv2.CascadeClassifier("C:/Users/p Kumar/Desktop/py/haarcascade_template.xml")

img = cv2.imread("C:/Users/p Kumar/Desktop/py/sample.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

# print(type(faces))
# print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 5)


cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()