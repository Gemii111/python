import pygame
import threading
import requests
import cv2
from x52 import x52

CAMERA_IP = '192.168.1.223'
CAMERA_PORT = 80
# Rtsp_Url = 'rtsp://admin:P@ssw0rd@192.168.1.223/ONVIF/MediaInput?profile=3_def_profile6'
Rtsp_Url='rtsp://admin:P@ssw0rd@192.168.1.227/ONVIF/MediaInput?profile=def_profile1'

Cam = cv2.VideoCapture(Rtsp_Url, cv2.CAP_FFMPEG)
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
    iszoom = False

    while True:
        pygame.event.pump()

        # Control pan
        if x_axis > 0.1 or x_axis < -0.1:
            pan_speed = int(x_axis * 100 * SPEED)
            requests.get(CGI_URL + PanCgi + f'{pan_speed}')
            ispan = True
        else:
            if ispan:
                requests.get(CGI_URL + PanCgi + f'{0}')
                ispan = False

        # Control tilt
        if y_axis > 0.1 or y_axis < -0.1:
            tilt_speed = int(y_axis * 100 * SPEED)
            requests.get(CGI_URL + TiltCgi + f'{tilt_speed}')
            istilt = True
        else:
            if istilt:
                requests.get(CGI_URL + TiltCgi + f'{0}')
                istilt = False

        # Control zoom
        zoom_in_button = joystick.get_button(0)
        zoom_out_button = joystick.get_button(4)

        if zoom_in_button and not iszoom:
            requests.get(CGI_URL + ZoomCgi + '3')
            iszoom = True
        elif zoom_out_button and not iszoom:
            requests.get(CGI_URL + ZoomCgi + '-3')
            iszoom = True
        elif iszoom:
            requests.get(CGI_URL + ZoomCgi + '0')
            iszoom = False


thread = threading.Thread(target=check_axis_value)
thread.start()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            quit()
    ret, frame = Cam.read()

    if not ret:
        print("Error reading frame")
        break

    cv2.imshow('PTZ Camera Stream', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)

Cam.release()

cv2.destroyAllWindows()
