import pygame
import threading
import requests
import cv2

CAMERA_IP = '192.168.1.223'
CAMERA_PORT = 80
rtsp_url2 = 'rtsp://admin:P@ssw0rd@192.168.1.223/ONVIF/MediaInput?profile=3_def_profile6'
cam = cv2.VideoCapture(rtsp_url2, cv2.CAP_FFMPEG)
IP_ADDRESS = '192.168.1.223'
CGI_URL = f'http://{IP_ADDRESS}/cgi-bin/'
PanCgi = 'directctrl?rpan='
TiltCgi = 'directctrl?rtilt='
ZoomCgi = 'directctrl?zoom='
lastcommand = ''
SPEED = 2

pygame.init()

pygame.display.set_caption("Joystick X52")


joystick = pygame.joystick.Joystick(0)
joystick.init()


x_axis = 0
y_axis = 0


def check_axis_value():
    global x_axis
    global y_axis

    ispan = False
    istilt = False

    while True:
        pygame.event.pump()
        if x_axis > 0.1 or x_axis < 0.1:
            pan_speed = int(x_axis * 100 * SPEED)
            requests.get(CGI_URL + PanCgi + f'{pan_speed}')
            ispan = True
        else:
            if ispan:
                requests.get(CGI_URL + PanCgi + f'{0}')

        if y_axis > 0.1 or y_axis < 0.1:
            tilt_speed = int(y_axis * 100 * SPEED)
            requests.get(CGI_URL + TiltCgi + f'{tilt_speed}')
            istilt = True
        else:
            if istilt:
                requests.get(CGI_URL + TiltCgi + f'{0}')


thread = threading.Thread(target=check_axis_value)
thread.start()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            quit()
    ret, frame = cam.read()

    if not ret:
        print("Error reading frame")
        break

    cv2.imshow('PTZ Camera Stream', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)

cam.release()

cv2.destroyAllWindows()
