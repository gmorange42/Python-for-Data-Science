import cv2 as cv
import numpy as np


def check_extention(path: str) -> bool:
    '''check if the extention is jpg or jpeg'''
    return path.endswith('.jpg') or path .endswith('jpeg')


def ft_load(path: str) -> np.ndarray:
    '''open a image and print the shape and a pixels summary'''
    try:
        assert check_extention(path)
        im = cv.imread(path)
        assert isinstance(im, np.ndarray)
        print("The shape of image is:", im.shape)
        print(cv.cvtColor(im, cv.COLOR_BGR2RGB))
        return im
    except AssertionError:
        print("AssertionError: the file must be in jpg or jpeg format")


def main():
    '''main function to launch program'''
    print(ft_load("../images/animal.jpeg"))


if __name__ == '__main__':
    main()
