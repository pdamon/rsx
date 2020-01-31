import cv2


def main():
    with open("outputs.txt", "w+") as out:
        f = cv2.VideoCapture("pong.mp4")

        if not f.isOpened():
            print("error opening file")

        # frame_width = int(f.get(3))
        # frame_height = int(f.get(4))

        # output = cv2.VideoWriter("example.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30,(frame_width, frame_height))

        while f.isOpened():
            ret, frame = f.read()
            if ret:
                grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                ret, thresh = cv2.threshold(grayframe, 240, 255, cv2.THRESH_BINARY)

                contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                if len(contours) != 0:
                    c = max(contours, key=cv2.contourArea)
                    moments = cv2.moments(c)

                    if moments['m00'] != 0:
                        x = int(moments['m10'] / moments['m00'])
                        y = int(moments['m01'] / moments['m00'])

                        # cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

                        out.write("x:{} y:{}\n".format(x, y))

                    # cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
                    # output.write(frame)
                    # cv2.imshow("With Contours", frame)

                    # if cv2.waitKey(25) & 0xFF == ord('q'):
                        # break
            else:
                break

        f.release()
        # output.release()

        # cv2.destroyAllWindows()

    out.close()


if __name__ == '__main__':
    main()
