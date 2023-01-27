[![Security Status](https://www.murphysec.com/platform3/v3/badge/1612448969049812992.svg?t=1)](https://www.murphysec.com/accept?code=18595fc71688bb8a5e33d73533679ddf&type=1&from=2&t=2)

# License Location and Segmentation

Hi, everyone!❤🧡💛💚💙💜

This is my first project!✔

> This is the project of license plate location and segmentation. Actually, this is my experiment with digital image processing course. Through thinking about some basic algorithm ideas and the process of constantly adjusting parameters, I successfully completed this project.





# Notification

* The "test.jpg" is the original image, and the "bin_img.jpg" is a picture that I preprocessed.
* When you run script `"segment.py"`,you can see two windows as follow，also every character will be saved in your directory.

![image](https://user-images.githubusercontent.com/76271045/147907507-0ea9bad0-ca20-499a-acd5-294fcc067569.png)

![image](https://user-images.githubusercontent.com/76271045/147907606-543f6e1b-bd84-49d4-863b-42b4b9b14efa.png)

The second window shows the characters of the license plate segmentation. If you want to  display each character separately, you can modify my code to achieve.





# How to segment？

### 1.Preprocessing

This setp includes `gray conversion`, `threshold processing` and `orphological operation`. 

### 2.Traverse the image by column

If the sum of a certain column of pixels is `0`, it can be used as the position of the `dividing line`.

### 3.Difference

Since only one dividing line needs to be located between the characters, the `difference method` is used here to remove the continuous lines: all continuous values with a difference less than `D` are set to the first value in the range, and then the duplicates are removed.

### 4.Trick

Through the `difference`, we can successfully cut the characters, but there is `an annoying separator`. I used a special judgment. Traverse the lines, extract the ROI of each part, display and save characters through formatting control.

---

Tips:   The above is the character segmentation, and the next is the positioning of the license plate.😛😛

Are you ready?





# How to locate？

### 1.Image preprocessing

* `Low-Pass Filtering`: to remove noise;
* `OTSU and Canny`: to detect edges;

### 2.Morphological operations

Remove some black holes in the characters and noise.

### 3.FindContours  and draw

What's the most important thing is to find the correct ratio of the liscense?

Through testing here, I found that `the ratio of 3.5 to 4` is the best.

In addition, the size of the license plate of a small car is `440mm×140mm` in our country.





# Result

When you run script "locate.py", you will see windows as follow:

![image-20220103175207359](https://user-images.githubusercontent.com/76271045/147918727-ca84591e-eb9b-4801-b356-cc557e485aa0.png)




When you run script `main.py`, you will see `every character `as follow:

![image-20220103175824434](https://user-images.githubusercontent.com/76271045/147918795-0c14d3c9-58df-4108-a20d-aaf1634fa3fc.png)

![image-20220103175839575](https://user-images.githubusercontent.com/76271045/147918814-f294b029-d142-40e0-a74d-9131c1add751.png)



<u>A character will appear every time you enter!</u>

---

Finally，we will see the windows of  such liscense plate!

![image-20220103180053089](https://user-images.githubusercontent.com/76271045/147918831-e27bb3a2-f750-4248-8fde-36abc32f3797.png)



**Tips:**You can adjust the parameters to observe the positioning effect.





# Welfare

I integrated "segment.py" with "locate.py", that called `"main.py"`.





# At the end

Since it is the first time for me to work on a project, I don't have much experience. 

So, If there is any unreasonable description, please correct me~~
Thank you very much!!😂😂