import cv2


class MyClass:
    def __init__(self):

        with open('D:\python\open cv\prtsp.txt', 'r') as f:
            for line in f:
                rtsp_url = line.strip()

        self.cam1 = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
        while True:
            ret1, frame1 = self.cam1.read()

            if not ret1:
                print("Error reading frame")
                break

            cv2.imshow('PTZ Camera Stream 1', frame1)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        self.cam1.release()

        cv2.destroyAllWindows()













        

    # def show(self):
    #     while True:
    #         ret1, frame1 = self.cam1.read()

    #         if not ret1:
    #             print("Error reading frame")
    #             break

    #         cv2.imshow('PTZ Camera Stream 1', frame1)

    #         key = cv2.waitKey(1)
    #         if key == ord('q'):
    #             break

    #     self.cam1.release()

    #     cv2.destroyAllWindows()
