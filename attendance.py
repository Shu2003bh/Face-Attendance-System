import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
# Initialize video capture
video_capture = cv2.VideoCapture(0)
# Load and encode the known face
sir_image = face_recognition.load_image_file("C:\\Users\\shubh\\python\\faceattendance\\image\\sir.jpeg")
Adarsh_image = face_recognition.load_image_file("C:\\Users\\shubh\\python\\faceattendance\\image\\ADARSH.jpg")
Shubham_image = face_recognition.load_image_file("C:\\Users\\shubh\\python\\faceattendance\\image\\Shubham.jpg")
sir_encodings = face_recognition.face_encodings(sir_image)
Adarsh_encodings = face_recognition.face_encodings(Adarsh_image)
Shubham_encodings = face_recognition.face_encodings(Shubham_image)
# Load and encode the known face
if len(sir_encodings) == 0:
    raise ValueError("No face found in the known image. Please check the image file.")
# Initialize known face information
sir_encodings = sir_encodings[0]
Adarsh_encodings = Adarsh_encodings[0]
Shubham_encodings = Shubham_encodings[0]
known_face_encoding = [sir_encodings]
known_face_encoding = [Adarsh_encodings]
known_face_encoding = [Shubham_encodings]
known_faces_names = ["sir"]
known_faces_names = ["ADARSH_Axis_DS_FY"]
known_faces_names = ["Shubham_Axis_DS_FY"]
students = known_faces_names.copy()
# Set up CSV file for writing
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
csv_file = open(current_date + '.csv', 'w+', newline='')
lnwriter = csv.writer(csv_file)
# Initialize variables
face_locations = []
face_encodings = []
face_names = []
frame_counter = 0
frame_skip = 5  # Process every 5th frame
while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()

    if not ret:
        break

    frame_counter += 1
    if frame_counter % frame_skip == 0:
        # Resize frame to speed up face recognition
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

        # Find all face locations and encodings in the frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    current_time = datetime.now().strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

    # Draw the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left, top - 10), font, 0.75, (255, 255, 255), 2)

    # Display the frame
    cv2.imshow("Attendance System", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
csv_file.close()
