from load_image import ft_load
import cv2 as cv
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    '''Inverts the color of the image received.'''
    try:
        assert isinstance(array, np.ndarray)
        invert = array.copy()
        lrow, lcol, _ = invert.shape
        for x in range(lrow):
            for y in range(lcol):
                invert[x][y][0] = 255 - invert[x][y][0]
                invert[x][y][1] = 255 - invert[x][y][1]
                invert[x][y][2] = 255 - invert[x][y][2]
        cv.imshow("invertLandscape.jpg", invert)
        cv.waitKey(0)
    except AssertionError:
        print("AssertionError: error with the image \
(don't existe, not a jpg or jpeg")


def ft_red(array: np.ndarray) -> np.ndarray:
    '''Changes the image received to red.'''
    try:
        assert isinstance(array, np.ndarray)
        red = array.copy()
        lrow, lcol, _ = red.shape
        for x in range(lrow):
            for y in range(lcol):
                red[x][y][0] = 0
                red[x][y][1] = 0
        cv.imshow("redLandscape.jpg", red)
        cv.waitKey(0)
    except AssertionError:
        print("AssertionError: error with the image \
(don't existe, not a jpg or jpeg")


def ft_green(array: np.ndarray) -> np.ndarray:
    '''Changes the image received to green.'''
    try:
        assert isinstance(array, np.ndarray)
        green = array.copy()
        lrow, lcol, _ = green.shape
        for x in range(lrow):
            for y in range(lcol):
                green[x][y][0] = 0
                green[x][y][2] = 0
        cv.imshow("greenLandscape.jpg", green)
        cv.waitKey(0)
    except AssertionError:
        print("AssertionError: error with the image \
(don't existe, not a jpg or jpeg")


def ft_blue(array: np.ndarray) -> np.ndarray:
    '''Changes the image received to blue.'''
    try:
        assert isinstance(array, np.ndarray)
        blue = array.copy()
        lrow, lcol, _ = blue.shape
        for x in range(lrow):
            for y in range(lcol):
                blue[x][y][1] = 0
                blue[x][y][2] = 0
        cv.imshow("blueLandscape.jpg", blue)
        cv.waitKey(0)
    except AssertionError:
        print("AssertionError: error with the image \
(don't existe, not a jpg or jpeg")


def ft_grey(array: np.ndarray) -> np.ndarray:
    '''Changes the image received to grey.'''
    try:
        assert isinstance(array, np.ndarray)
        grey = array.copy()
        lrow, lcol, _ = grey.shape
        for x in range(lrow):
            for y in range(lcol):
                grey[x][y][0] = grey[x][y][1]
                grey[x][y][2] = grey[x][y][1]
        cv.imshow("greyLandscape.jpg", grey)
        cv.waitKey(0)
    except AssertionError:
        print("AssertionError: error with the image \
(don't existe, not a jpg or jpeg")


def main():
    '''Make some tests'''
    try:
        array = ft_load("../images/landscape.jpg")
        assert isinstance(array, np.ndarray)
        cv.imshow("landscape.jpg", array)
        cv.waitKey(0)
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
        print(ft_red.__doc__)
        print(ft_green.__doc__)
        print(ft_blue.__doc__)
        print(ft_grey.__doc__)
    except AssertionError:
        print("AssertionError: error with the image \
(don't existe, not a jpg or jpeg")


if __name__ == '__main__':
    main()
