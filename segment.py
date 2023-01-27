import cv2 as cv
from skimage import io
from matplotlib import pyplot as plt

img = io.imread("data/bin_img.jpg")

res = img.copy()
src = res[45:190, 30:650]
rows, cols = src.shape[:2]

pixel_nums = []
for i in range(cols):
    s = 0
    for j in range(rows):
        s += src[j, i]
    if s[0] == 0:  # 排除像元皆为零的列
        pixel_nums.append(i)
    s = 0

# 去除连续的分割线条：将差值小于D的所有连续值设置为该范围内第一个值，然后去重
D = 20
for j in range(len(pixel_nums) - 1):
    if abs(pixel_nums[j] - pixel_nums[j + 1]) < D:
        pixel_nums[j + 1] = pixel_nums[j]

sorted_list = list(set(pixel_nums))
sorted_list.sort(key=pixel_nums.index)

num = 1
for k in range(len(sorted_list) - 1):
    if abs(sorted_list[k] - sorted_list[k + 1]) < 75:  # 根据差值,排除干扰元素分隔符
        continue

    # cv.line(src, (sorted_list[k], 0), (sorted_list[k], cols), (0, 255, 255), 1)  # 绘制分割线以便参考
    dst = src[0:rows, sorted_list[k]:sorted_list[k + 1]]  # 提取每一部分的ROI

    plt.figure("output")
    plt.subplot(1, len(sorted_list) - 4, num)  # 同屏显示分割的字符
    plt.axis("off")
    plt.imshow(dst)
    cv.imwrite("res/char{}.jpg".format(num), dst)
    num = num + 1

# 显示原图
plt.figure("Input", figsize=(5, 2))
plt.title("License plate")
plt.axis("off")
plt.imshow(img)

plt.show()
