#import numpy as np
import cv2


def main():
    cap = cv2.VideoCapture(0)

    while True:
        # capture frame by frame
        ret, frame = cap.read()

        # our operations on the frame come here (????)
        gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)

        # display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # when everyting done, relase the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
