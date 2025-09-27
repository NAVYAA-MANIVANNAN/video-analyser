from ultralytics import YOLO
import cv2

# Load a pre-trained YOLOv8 model
model = YOLO('yolov8n.pt')

# Access the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Run YOLO inference on the frame
        results = model(frame)

        # Draw the results on the frame
        annotated_frame = results[0].plot()

        # Display the frame
        cv2.imshow("YOLO Live Feed", annotated_frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows() 