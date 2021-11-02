import cv2
import time

cascade_src = 'cars.xml'
# video = 'data/Cars_On_Highway.mp4'
video = 'data/video1.avi'
# video = 'data/video2.avi'


def detectCars(filename):
  rectangles = []
  cascade = cv2.CascadeClassifier(cascade_src)

  vc = cv2.VideoCapture(filename)

  if vc.isOpened():
      rval , frame = vc.read()
  else:
      rval = False


  while rval:
    rval, frame = vc.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # car detection
    cars = cascade.detectMultiScale(gray, 1.3, 3)
	
    if len(cars) > 0:
      print("Car detected at " + str(vc.get(cv2.CAP_PROP_POS_MSEC)/1000) + "seconds")
      time.sleep(2)

    if cv2.waitKey(33) == ord('q'):
      break

  vc.release()


detectCars(video)

