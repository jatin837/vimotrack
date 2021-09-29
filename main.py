from helper.parse_cli import get_cli_args
from imutils.video import VideoStream
import datetime
import time
import cv2

if __name__ == "__main__":

    (ipath, area) = get_cli_args()

    if len(ipath) == 0:
        v_source = VideoStream(src=0).start()
        time.sleep(2.0)

    else:
        v_source = cv2.VideoCapture(ipath)

    firstFrame = None
