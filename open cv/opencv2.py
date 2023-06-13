
import cv2

# RTSP URL with PTZ credentials
rtsp_url2 = 'rtsp://admin:P@ssw0rd@192.168.1.223/ONVIF/MediaInput?profile=3_def_profile6'


# Open RTSP stream
cam = cv2.VideoCapture(rtsp_url2, cv2.CAP_FFMPEG)


# Main loop
while True:
    # Read frames from the stream
    ret, frame = cam.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error reading frame")
        break

    # Display the frame
    cv2.imshow('PTZ Camera Stream', frame)

    # Control PTZ camera's movement
    key = cv2.waitKey(1)
    if key == ord('q'):
      break  
      
    
    

# Release the stream
cam.release()

cv2.destroyAllWindows()