import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def manual_histogram(image):
    image = image.ravel()  # 降维

    d = {}  # 统计频次
    for i in image:
        d[i] = d.get(i, 0) + 1

    items = list(d.items())  # 字典转化为列表并根据元素值升序排序
    items.sort(key=lambda x: x[0])

    pixels_count = image.shape[0]

    x_data = [i[0] for i in items]
    y_data = [i[1] / pixels_count for i in items]

    print(x_data)
    print(y_data)

    fig = plt.figure(figsize=(8, 5))
    fig.canvas.set_window_title('Manual GRAY Histogram')
    plt.xlabel("gray level")
    plt.ylabel("Absolute quantity")
    plt.bar(x=x_data, height=y_data)


if __name__ == '__main__':
    src = np.array([[0, 1, 3, 2, 1, 3, 2, 1],
                    [0, 5, 7, 6, 2, 5, 6, 7],
                    [1, 6, 0, 6, 3, 5, 1, 2],
                    [2, 6, 7, 5, 3, 6, 5, 0],
                    [3, 2, 2, 7, 2, 4, 1, 6],
                    [2, 2, 5, 6, 2, 7, 6, 0],
                    [1, 2, 3, 2, 1, 2, 1, 2],
                    [3, 1, 2, 3, 1, 2, 2, 1]], dtype=np.uint8)

    test = cv.imread("test.jpg", 0)
    manual_histogram(test)

    # 与直接调用plt.hist()作比较
    fig = plt.figure(figsize=(8, 5))
    fig.canvas.set_window_title("PLT Histogram")
    plt.hist(test.ravel(), bins=255, density=True)

    plt.show()
