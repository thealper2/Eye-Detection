import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("frontalface.xml")
eye_cascade = cv2.CascadeClassifier("eye.xml")

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (480, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for face in faces:
        (x, y, w, h) = face

    face_image = frame[y:y+h, x:x+w]
    gray_face = gray[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(gray_face)

    for eye in eyes:
        (x, y, w, h) = eye
        cv2.rectangle(face_image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("Video", frame)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
