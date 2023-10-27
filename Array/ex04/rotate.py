import load_image as load_image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def rotate(im: np.ndarray) -> tuple:
    '''Transposes image, adds axes and prints it, its shape and its pixels '''
    assert isinstance(im, np.ndarray)
    lrow, lcol = im.shape
    temp = list()
    row = list()
    for y in range(lcol):
        for x in range(lrow):
            row.append(im[x][y])
        temp.append(row.copy())
        row.clear()
    im = np.array(temp)
    plt.imshow(cv.cvtColor(im, cv.COLOR_BGR2RGB))
    plt.show()
    print("New shape after Transpose:", im.shape)
    print(im)


def main():
    '''call load_image() and call rotate()'''
    try:
        im = load_image.ft_load('../images/animalSliced.jpeg')
        rotate(im)
    except AssertionError:
        print("AssertionError: the file must be in jpg or jpeg format")


if __name__ == '__main__':
    main()
