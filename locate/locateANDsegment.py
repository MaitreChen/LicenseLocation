from skimage import color, filters
from skimage.morphology import disk
import numpy as np
import cv2 as cv


# 基于灰度图的形态学变换定位车牌
# 图片预处理
def image_preprocessing(img):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 低通滤波、去噪
    gaussian_blur = cv.GaussianBlur(gray_img, (11, 11), 0, 0)
    median_blur = cv.medianBlur(gaussian_blur, ksize=3)

    # otsu二值化，边缘检测
    retval, binary = cv.threshold(median_blur, 0, 255, cv.THRESH_OTSU)
    edge = cv.Canny(binary, 200, 250)

    # 形态学运算
    convolution_kernel = np.ones((9, 9), np.uint8)
    dst1 = cv.morphologyEx(edge, cv.MORPH_CLOSE, convolution_kernel)  # 闭运算去除前景中的小孔
    dst2 = cv.morphologyEx(dst1, cv.MORPH_OPEN, convolution_kernel)  # 开运算去除噪声

    return dst2


# 查找轮廓
def find_contours(dst):
    contours, hierarchy = cv.findContours(dst, cv.RETR_EXTERNAL, 2)

    con_ls = []
    for c in contours:
        x, y, w, h = cv.boundingRect(c)  # 轮廓信息转换
        ratio = w / h  # 获得车牌比例
        if ratio < 3.5 or ratio > 4:
            continue
        con_ls.append([x, y, w, h])

        return con_ls


# 绘制车牌框
def draw_contours(x, y, w, h):
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    global res
    res = src[y:y + h, x:x + w]  # 作为返回值以便字符的切割

    cv.imshow("result", img)
    cv.imwrite("result.jpg",res)
    cv.waitKey()

    return res


# 车牌预处理，去噪并阈值化
def license_plate_preprocessing(img):
    gray_image = color.rgb2gray(img)
    gaussian_filter = filters.gaussian(gray_image, sigma=5)
    median_filter = filters.median(gaussian_filter, disk(3))

    threshold = filters.threshold_otsu(median_filter, nbins=256)
    dst = (gray_image > threshold) * 1.0

    return dst


def segment(dst):
    rows, cols = dst.shape[:2]

    # 按列统计像元
    pixel_nums = []
    for i in range(cols):
        s = 0
        for j in range(rows):
            s += dst[j, i]
        if s < 10:
            pixel_nums.append(i)
        s = 0

    # 去除连续的分割线条
    D = 10
    for j in range(len(pixel_nums) - 1):
        if abs(pixel_nums[j] - pixel_nums[j + 1]) < D:
            pixel_nums[j + 1] = pixel_nums[j]

    sorted_list = list(set(pixel_nums))
    sorted_list.sort(key=pixel_nums.index)

    num = 1  # 用于标记分隔符的位置并跳过此区域
    flag = 0
    for k in range(len(sorted_list) - 1):
        if abs(sorted_list[k] - sorted_list[k + 1]) <= 10:  # 根据差值,寻找干扰元素
            flag += 1
        if flag == 3:
            sorted_list.remove(sorted_list[k])
            k -= 1
    # print(sorted_list)

    for k in range(len(sorted_list) - 1):
        # cv.line(src, (sorted_list[k], 0), (sorted_list[k], cols), (0, 255, 255), 1)  # 绘制分割线以便参考

        if num != 3:  # 排除分隔符
            dst = res[0:rows, sorted_list[k]:sorted_list[k + 1]]  # 提取每一部分的ROI
            cv.imshow("char{}".format(num), dst)
            cv.waitKey()

        num = num + 1
    cv.destroyAllWindows()


if __name__ == '__main__':
    img = cv.imread("License plate.jpg")
    src = img.copy()

    dst1 = image_preprocessing(img)  # 图像预处理
    contours_ls = find_contours(dst1)  # 轮廓查找，返回x,y,w,h

    x, y, w, h = contours_ls[0][0], contours_ls[0][1], contours_ls[0][2], contours_ls[0][3]
    license_plate = draw_contours(x, y, w, h)  # 绘制车牌边框,并返回边框

    dst2 = license_plate_preprocessing(license_plate)  # 车牌图像预处理
    segment(dst2)  # 车牌字符的分割

    cv.imshow("license_plate", license_plate)

    cv.waitKey()
    cv.destroyAllWindows()
