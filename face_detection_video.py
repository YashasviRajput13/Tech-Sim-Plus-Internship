import cv2
import cv2.data
import random
import time

# Load model
model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start camera
cam = cv2.VideoCapture(0)

# For FPS calculation
prev_time = 0

# Store colors for faces (to avoid flickering)
face_colors = {}

# Toggle mode
blur_mode = False

def get_color(face_id):
    if face_id not in face_colors:
        face_colors[face_id] = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
    return face_colors[face_id]

while True:
    status, frame = cam.read()
    if not status:
        print("Camera not found")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = model.detectMultiScale(gray, 1.3, 5)

    # Assign IDs (simple indexing)
    for i, (x, y, w, h) in enumerate(faces):

        color = get_color(i)

        if blur_mode:
            # Blur face (privacy mode 🔐)
            face_region = frame[y:y+h, x:x+w]
            face_region = cv2.GaussianBlur(face_region, (99, 99), 30)
            frame[y:y+h, x:x+w] = face_region
        else:
            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

            # Stylish label background
            cv2.rectangle(frame, (x, y-30), (x+w, y), color, -1)

            # Label text
            cv2.putText(frame,
                        f"Face {i+1}",
                        (x+5, y-8),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (255,255,255),
                        2,
                        cv2.LINE_AA)

    # FPS calculation ⚡
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    # Display FPS
    cv2.putText(frame,
                f"FPS: {int(fps)}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2)

    # Display face count
    cv2.putText(frame,
                f"Faces: {len(faces)}",
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2)

    # Mode display
    mode_text = "BLUR MODE" if blur_mode else "DETECTION MODE"
    cv2.putText(frame,
                mode_text,
                (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2)

    # Show window
    cv2.imshow("AI Face System", frame)

    key = cv2.waitKey(1) & 0xFF

    # Controls 🎮
    if key == ord('q'):
        break
    elif key == ord('b'):
        blur_mode = not blur_mode  # toggle blur

# Cleanup
cam.release()
cv2.destroyAllWindows()