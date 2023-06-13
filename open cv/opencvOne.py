import cv2

with open('D:\python\open cv\prtsp.txt', 'r') as f:
    for line in f:
        rtsp_url = line.strip()


cam = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)


while True:
    ret, frame = cam.read()

    if not ret:
        print("Error reading frame")
        break

    cv2.imshow('PTZ Camera Stream', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
cam.release()

cv2.destroyAllWindows()