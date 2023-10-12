import cv2


class Cam:
    def __init__(self,camNum) -> None:
        self.camNum = camNum
        self.cap = cv2.VideoCapture(self.camNum)

    def open(self):
        while True:
            ret, frame = self.cap.read()

            if not ret:
                break

            if cv2.waitKey(1) & 0xff == ord('q'):
                break
            cv2.imshow('Camera Feed', frame)

        self.cap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    cam = Cam(2)
    cam.open()