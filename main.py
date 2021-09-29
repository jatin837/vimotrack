from helper.parse_cli import get_cli_args
from imutils.video import VideoStream
import datetime
from PIL import Image as im
import time
import cv2

if __name__ == "__main__":

    (ipath, area) = get_cli_args()

    if len(ipath) == 0:
        v_source = VideoStream(src=0).start()

    else:
        v_source = cv2.VideoCapture(ipath)

    first_frame = None
    i =0
    while True:
        frame = v_source.read()
        time.sleep(0.5)
        data = im.fromarray(frame)
        data.save(f'{i}.png')
        i += 1
        print(i)
