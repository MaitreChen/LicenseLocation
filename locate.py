import cv2 as cv
import numpy as np

# 基于灰度图的形态学变换定位车牌
img = cv.imread("data/license-plate.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 低通滤波、去噪
gaussian_blur = cv.GaussianBlur(gray_img, (11, 11), 0, 0)
median_blur = cv.medianBlur(gaussian_blur, ksize=3)

# threshold and canny
ret, binary = cv.threshold(median_blur, 0, 255, cv.THRESH_OTSU)
edge = cv.Canny(binary, 200, 250)

# 形态学运算
convolution_kernel = np.ones((9, 9), np.uint8)
dst1 = cv.morphologyEx(edge, cv.MORPH_CLOSE, convolution_kernel)  # 闭运算去除前景中的小孔
dst2 = cv.morphologyEx(dst1, cv.MORPH_OPEN, convolution_kernel)  # 开运算去除噪声

# 查找轮廓
contours, hierarchy = cv.findContours(dst2, cv.RETR_EXTERNAL, 2)
for c in contours:
    x, y, w, h = cv.boundingRect(c)  # 轮廓信息转换
    ratio = w / h  # 获得车牌比例
    if ratio < 3.5 or ratio > 4:
        continue
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 绘制车框

# cv.imshow("gray_img",gray_img)
# cv.imshow("gaussian_blur",gaussian_blur)
# cv.imshow("binary", binary)
# cv.imshow("edge",edge)
# cv.imshow("dilate_img", dilate_img)
# cv.imshow("erode_img", erode_img)
cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()
