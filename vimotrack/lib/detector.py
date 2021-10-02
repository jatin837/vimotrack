import numpy
import cv2

def frame_diff(r_frame:numpy.ndarray, c_frame:numpy.ndarray) -> numpy.ndarray:
    """
    r_frame: reference frame
    c_frame: current frame
    return:  difference between r_frame and c_frame
    """
    return cv2.absdiff(r_frame, c_frame)

def apply_gray(frame:numpy.ndarray) -> numpy.ndarray:
    """
    return: grayscale image as numpy ndarray
    """
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def resize(frame: numpy.ndarray, width: int) -> numpy.ndarray:
    """
    frame: input frame(BGR format L X W X 3)
    width: pxl width
    return: resized image in numpy ndarray
    """
    return cv2.resize(frame, width=width)

def gaussian_blur(frame: numpy.ndarray, k_size:tuple, sigma: int) -> numpy.ndarray:
    """
    NOTE: I don't understand very well, how passing sigma as 0 will let opencv determine
    sigma value based on kernal size
    """
    return cv2.GaussianBlur(frame, k_size, sigma)
