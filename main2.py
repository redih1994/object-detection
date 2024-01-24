import os
import cv2
import time
from emailing import send_email
from threading import Thread

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

time.sleep(1)
status_list = []
count = 1
image_with_obj = None  # Initialize image_with_obj


def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)


while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the current frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        status = 1
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Save the frame when a face is detected
        cv2.imwrite(f"images/{count}.png", frame)
        count += 1

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list == [1, 0]:
        email_thread = Thread(target=send_email, args=(image_with_obj,))
        email_thread.daemon = True
        email_thread.start()

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
clean_folder()
cv2.destroyAllWindows()
