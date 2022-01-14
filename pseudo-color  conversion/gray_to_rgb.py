import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def gray_to_blue(x):
    if 0 <= x <= 64:
        return 255
    elif 64 < x <= 128:
        return -4 * x + 512
    elif 128 < x <= 255:
        return 0


def gray_to_green(x):
    if 0 <= x <= 64:
        return 4 * x
    elif 64 < x <= 192:
        return 255
    elif 192 < x <= 255:
        return -4 * x + 1024


def gray_to_red(x):
    if 0 <= x <= 128:
        return 0
    elif 128 < x <= 192:
        return 4 * x - 512
    elif 192 < x <= 255:
        return 255


def transformer(image):
    rows, cols = image.shape
    color = np.zeros((rows, cols, 3), np.uint8)
    for i in range(rows):
        for j in range(cols):
            color[i, j, 0] = gray_to_blue(image[i, j])
            color[i, j, 1] = gray_to_green(image[i, j])
            color[i, j, 2] = gray_to_red(image[i, j])

            # color[i, j, 0] = r
            # color[i, j, 1] = g
            # color[i, j, 2] = b
    return color


if __name__ == '__main__':
    src = cv.imread("astronaut.jpg")
    gray_img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    color_image = transformer(gray_img)
    color_image = cv.cvtColor(color_image, cv.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 8))
    plt.subplot(131)
    plt.title("origin image")
    plt.axis("off")
    src = cv.cvtColor(src, cv.COLOR_BGR2RGB)
    plt.imshow(src)

    plt.subplot(132)
    plt.title("gray image")
    plt.axis("off")
    plt.imshow(gray_img, cmap='gray')

    plt.subplot(133)
    plt.title("false color image")
    plt.axis("off")
    plt.imshow(color_image)

    plt.show()
