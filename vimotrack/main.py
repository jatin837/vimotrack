from helper.parse_cli import get_cli_args
from imutils.video import VideoStream
import datetime
from PIL import Image as im
import time
import cv2
from detector import Detector

if __name__ == "__main__":

    while(True):
        print("Press b to begin and q to exit")
        res = input()
        if res == 'b':
            print('wait')
            break
        elif res == 'q':
            exit()
        else:
            print('enter valid input')

    (ipath, area) = get_cli_args()

    if len(ipath) == 0:
        v_source = VideoStream(src=0).start()

    else:
        v_source = cv2.VideoCapture(ipath)

    first_frame = None

    while True:
        frame = v_source.read()
        time.sleep(0.5)
