from cv2 import CAP_PROP_XI_CC_MATRIX_01
from donkeycar.vehicle import Vehicle
from fullspeed import CvCam
import donkeycar.utils
import cv2
V = Vehicle()

cam = CvCam()

V.add(cam, inputs=['camera/image'], outputs=['throttle'])

V.start()



