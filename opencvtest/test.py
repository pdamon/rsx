import cv2
import numpy as np
from matplotlib import pyplot as plot


def main():
    f = cv2.VideoCapture("pong.mp4")

    if not f.isOpened():
        print("error opening file")

    while f.isOpened():
        ret, frame = f.read()
        if ret:
            grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(grayframe, 200, 255, cv2.THRESH_BINARY)

            cv2.imshow("Frame", thresh)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    f.release()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
