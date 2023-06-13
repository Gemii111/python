import cv2


class MyClassTwo:
    def __init__(self):

        rtsp_url2 = 'rtsp://admin:P@ssw0rd@192.168.1.227/ONVIF/MediaInput?profile=def_profile1'
        rtsp_url3 = 'rtsp://admin:P@ssw0rd@192.168.1.223/ONVIF/MediaInput?profile=3_def_profile6'

        self.cam01 = cv2.VideoCapture(rtsp_url2, cv2.CAP_FFMPEG)
        self.cam02 = cv2.VideoCapture(rtsp_url3, cv2.CAP_FFMPEG)
        while True:
            ret1, frame1 = self.cam01.read()
            ret2, frame2 = self.cam02.read()

            if not ret1 or not ret2:
                print("Error reading frame")
                break

            cv2.imshow('PTZ Camera Stream 1', frame1)
            cv2.imshow('PTZ Camera Stream 2', frame2)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        self.cam01.release()
        self.cam02.release()

        cv2.destroyAllWindows()

   

