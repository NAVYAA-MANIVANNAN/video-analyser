import cv2

# Access the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam was opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    # Loop to continuously read frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Display the frame in a window
        cv2.imshow('Webcam Feed', frame)
        
        # Press 'q' to exit the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()