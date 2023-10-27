import load_image as load_image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def zoom(im: np.ndarray) -> None:
    '''grays the image, slices it, adds axes and prints it'''
    im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    im = im[100:500, 450:850]
    plt.imshow(cv.cvtColor(im, cv.COLOR_BGR2RGB), interpolation='none')
    plt.show()
    print("New shape after slicing:", im.shape)
    print(im)


def main():
    '''call load_image() and call zoom()'''
    try:
        im = load_image.ft_load('../images/animal.jpeg')
        zoom(im)
    except AssertionError:
        print("AssertionError: the file must be in jpg or jpeg format")


if __name__ == '__main__':
    main()
