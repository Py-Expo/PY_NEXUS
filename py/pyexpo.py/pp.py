import cv2 as cv

# Load pre-trained MobileNet SSD model for object detection
object_model_path = r"C:\path\to\frozen_inference_graph.pb"
graph_config_path = r"C:\path\to\graph_config.pbtxt"

object_model = cv.dnn.readNetFromTensorflow(object_model_path, graph_config_path)

# Load pre-trained Haar cascade classifier for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect objects and draw bounding boxes
def detect_objects(frame):
    # Resize frame to 300x300 (input size of MobileNet SSD)
    blob = cv.dnn.blobFromImage(cv.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    object_model.setInput(blob)
    detections = object_model.forward()
    
    # Loop over the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Confidence threshold
            # Get coordinates of the bounding box
            box = detections[0, 0, i, 3:7] * [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]
            (startX, startY, endX, endY) = box.astype("int")
            
            # Draw bounding box around the detected object
            cv.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
    
    return frame

# Function to detect faces and draw bounding boxes
def detect_faces(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Draw bounding box around detected faces
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return frame

# Capture video from default camera (0)
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect objects and faces and draw bounding boxes
    frame = detect_objects(frame)
    frame = detect_faces(frame)
    
    # Display the resulting frame
    cv.imshow('Object and Face Detection', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv.destroyAllWindows()
