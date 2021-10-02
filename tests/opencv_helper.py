from vimotrack.lib import detector
import cv2

def test_gray():
    img_path = "./assets/test.png"
    img = cv2.imread(img_path)
    gray = detector.apply_gray(img)
    assert(gray, cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))