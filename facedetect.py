import torch
import cv2
import numpy as np
import face_recognition

# Check if MPS (Apple Metal Performance Shaders) is available
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Using device: {device}")

# Load known faces and names
known_faces = []
known_names = []

# Load a sample image and encode the face
image_path = "/Users/hariharasudhan/Documents/WhatsApp Image 2023-08-15 at 9.59.37 AM.jpeg"  # Replace with your image path
known_image = face_recognition.load_image_file(image_path)
known_encoding = face_recognition.face_encodings(known_image)[0]

# Convert encoding to a PyTorch tensor with float32
known_encoding = torch.tensor(known_encoding, dtype=torch.float32, device=device)

known_faces.append(known_encoding)
known_names.append("Hari")  # Replace with the person's name

# Start Video Capture
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Convert encodings to PyTorch tensors (force float32 for MPS)
    face_encodings = [torch.tensor(encoding, dtype=torch.float32, device=device) for encoding in face_encodings]

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Unknown"

        # Compute distances using PyTorch
        distances = [torch.norm(face_encoding - known_face, p=2).item() for known_face in known_faces]
        
        if len(distances) > 0 and min(distances) < 0.6:  # Threshold for recognition
            match_index = distances.index(min(distances))
            name = known_names[match_index]

        # Draw bounding box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display output
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()