#!/usr/bin/python3

import cv2
from picamera2 import Picamera2


def main():
    # Grab images as numpy arrays and leave everything else to OpenCV.
    cv2.startWindowThread()

    cam = Picamera2()
    cam.configure(cam.create_preview_configuration(
        main={"format": 'XRGB8888', "size": (640, 480)}))
    cam.start()

    while True:
        im = cam.capture_array()
        #grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Camera", im)
        if cv2.waitKey(1) == ord('q'):
            break
    
    cam.close()


if __name__ == '__main__':
    main()
