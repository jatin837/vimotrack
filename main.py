from imutils.video import VideoStream
import argparse
import datetime
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", help="path to video file")
ap.add_argument("-a", "--area", help="minimum area size")
args = vars(ap.parse_args())

if args['input'] is None:
    vs = VideoStream(src=0).start()
    time.sleep(2.0)

else:
    vs = cv2.VideoCapture(args["input"])
