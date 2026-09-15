import cv2
import time

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

absence_before = False
absence_start = 0
warned = False

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access the camera.")
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for x, y, w, h in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (10, 0, 128),
            2
        )

    if len(faces) == 0:
        if not absence_before:
            absence_start = time.time()
            absence_before = True

        elapsed = time.time() - absence_start
        if elapsed > 5 * 60:
            if not warned:
                print("Warning: Camera absence detected!")
                warned = True
    else:
        absence_before = False
        warned = False

    cv2.putText(
        frame,
        f"Detected: {len(faces)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()