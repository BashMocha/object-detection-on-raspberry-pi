import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720


def main():
    camera = PiCamera()
    camera.resolution = (FRAME_WIDTH, FRAME_HEIGHT)
    camera.framerate = 10

    raw_capture = PiRGBArray(camera, size=(FRAME_WIDTH, FRAME_HEIGHT))
    raw_capture.truncate(0)

    for frame1 in camera.capture_continuous(raw_capture, format='bgr', use_video_port=True):

        t1 = cv2.getTickCount()

        # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
        # i.e. a single-column array, where each item in the column has the pixel RGB value
        frame = np.copy(frame1.array)
        frame.setflags(write=1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_expanded = np.expand_dims(frame_rgb, axis=0)

        # All the results have been drawn on the frame, so it's time to display it.
        cv2.imshow('Object detector', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break

        raw_capture.truncate(0)

    camera.close()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
