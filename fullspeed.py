import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


class CvCam(object):

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None
        throttle = 0
    
    def run(self):
            ret, self.frame = self.cap.read()
            throttle = 0
            faces = face_cascade.detectMultiScale(self.frame, scaleFactor=1.5, minNeighbors=5)
            gray =  cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            for (x, y, w, h) in faces:
                print(x, y, w, h)
                roi_gray = gray[y:y+h, x:x+w]
                img_item = "image.png"
                cv2.imwrite(img_item, roi_gray)
                color = (255, 0, 0) 
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(self.frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
                if(x < 250):
                    print("Left")
                if(x > 350):
                    print("Right")
                if(((x > 250 and x < 350)) or (w > 150 and h > 150)):
                    print("poop")
                    throttle=1.0
            return self.frame, throttle

class throotle(object):
    def __init__(self):
        throttle = 0

    def run(self):
        throttle = 1.0
        print(throttle)
        return throttle