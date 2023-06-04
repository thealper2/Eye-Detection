import cv2

image = cv2.imread("eye.png")

face_cascade = cv2.CascadeClassifier("frontalface.xml")
eye_cascade = cv2.CascadeClassifier("eye.xml")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for face in faces:
    (x, y, w, h) = face

face_image = image[y:y+h, x:x+w]
gray_face = gray[y:y+h, x:x+w]

eyes = eye_cascade.detectMultiScale(gray_face)

for eye in eyes:
    (x, y, w, h) = eye
    cv2.rectangle(face_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
