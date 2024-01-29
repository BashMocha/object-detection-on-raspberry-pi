import cv2
from picamera2 import Picamera2

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision


def main():
    pi_cam = Picamera2()
    pi_cam.preview_configuration.main.size = (1280, 720)
    pi_cam.preview_configuration.main.format = "RGB888"
    pi_cam.preview_configuration.main.align()
    pi_cam.configure('preview')

    pi_cam.start()
    while True:
        frame = pi_cam.capture_array()
        cv2.imshow('pi_cam', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()