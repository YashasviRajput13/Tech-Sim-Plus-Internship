# import cv2
# image = cv2.imread("image.png")
# image = cv2.resize(image,(500,500))
# cv2.imshow("image",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import cv2.data #to access the haarcascades files
import os  #to list the files in the directory
import time  # for FPS / detection time

print(os.listdir(cv2.data.haarcascades)) #to list the files in the haarcascades directory
image = cv2.imread("group.png")#to read the image

# Check if image loaded properly
if image is None:
    print("Image not found!")
    exit()

# Resize image for better performance
image = cv2.resize(image,(800,600))

# Convert image to grayscale (important for Haar cascade)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

training_file = "haarcascade_frontalface_default.xml" #to load the model
file_path = cv2.data.haarcascades + "/" + training_file
model = cv2.CascadeClassifier(file_path) #to load the model

# Start time (for performance measurement)
start_time = time.time()

faces = model.detectMultiScale(gray,1.3,5) #to detect the faces #1.3 is the scale factor #5 is the min neighbors
print(faces)

# End time → calculate detection time
end_time = time.time()
print("Detection Time:", round(end_time - start_time, 3), "seconds")

# Print total faces
print("Total Faces Detected:", len(faces))

# Loop through detected faces
for i, face in enumerate(faces):
    x1 = face[0]
    y1 = face[1]
    w = face[2]
    h = face[3]

    x2 = x1 + w
    y2 = y1 + h

    # Draw rectangle
    cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),2) #to draw the rectangle around the face (red)

    # Label background
    cv2.rectangle(image,(x1,y1-30),(x2,y1),(0,0,255),-1)

    # Face label
    cv2.putText(image,
                f"Face {i+1}",
                (x1+5,y1-8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255,255,255),
                2,
                cv2.LINE_AA)

    # Center point of face
    center_x = x1 + w//2
    center_y = y1 + h//2
    cv2.circle(image,(center_x,center_y),5,(255,0,0),-1)

    # Face dimensions
    cv2.putText(image,
                f"{w}x{h}",
                (x1,y2+20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0,255,255),
                1)

    # Optional blur (privacy mode)
    # face_region = image[y1:y2, x1:x2]
    # face_region = cv2.GaussianBlur(face_region,(51,51),20)
    # image[y1:y2, x1:x2] = face_region

# Display face count
cv2.putText(image,
            f"Faces: {len(faces)}",
            (10,30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2)

# Display detection time
cv2.putText(image,
            f"Time: {round(end_time - start_time,2)}s",
            (10,70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,0),
            2)

# Title
cv2.putText(image,
            "Face Detection System",
            (200,30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,255,255),
            2)

# Save output image
cv2.imwrite("output_faces.png",image)

# Show final image only (no comparison now)
cv2.imshow("Detected Faces",image)
cv2.waitKey(0)
cv2.destroyAllWindows()