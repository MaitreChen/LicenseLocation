# LicenseLocation

Hi,everyone!โค๐งก๐๐๐๐

This is my first project!โ
Actually,this is an assignment from my digital image processing experiment class.
Through thinking about algorithm ideas and the process of constantly adjusting parameters by myself, I successfully completed this project.

You can clone this project to local and run it.

## <u>Now,here is something to tell you:</u>

#### First, the "test.jpg" is the original image,and the "img.jpg" is a picture that i preprocessed.Among them,I used OTSU and morphological operations and so on

#### Second,when you run "segment.py",you can see two windows as follow๏ผalso every character will be saved in your directory.

![image](https://user-images.githubusercontent.com/76271045/147907507-0ea9bad0-ca20-499a-acd5-294fcc067569.png)

![image](https://user-images.githubusercontent.com/76271045/147907606-543f6e1b-bd84-49d4-863b-42b4b9b14efa.png)

*The second window shows the characters of the license plate segmentation. If you want to  display each character separately, you can modify my code to achieve.*



#### Thirdly, I will describe the algorithm idea of segmentation.๐

1.**Image preprocessing**,including gray conversion, threshold processing and orphological operation.(Of course, I also made a clever treatment to manually remove information that has nothing to do with characters.If there is no such operation, perhaps all the subsequent efforts will be wasted)

2.**Traverse the picture by column**, if the sum of a certain column of pixels is zero, then it can be used as the position of the dividing line.

3.Since only one dividing line needs to be located between the characters, the difference method is used here to remove the continuous lines: all continuous values with a difference less than D are set to the first value in the range, and then the duplicates are removed.

4.Through the third step, we can successfully cut the characters, but there is an annoying separator. I used a special judgment. Traverse the lines, extract the ROI of each part, display and save characters through formatting control.



---

**Tips:**   The above is the character segmentation, and the next is the positioning of the license plate.๐๐

Are you ready?



## Algorithm idea

### 1.Image preprocessing

Use low-pass filtering to remove noise๏ผOTSU thresholding๏ผand Canny to edge detecting

### 2.Morphological operations

Remove some black holes in the characters and remove noise.

### 3.FindContours  and draw

What's the most important thing is to find the correct ratio of the liscense.Through testing here, I found that the ratio of 3.5 to 4 is the best.(<u>According to the information available, in my country, the size of the license plate of a small car is **440mmร140mm**</u>)

---



## Result

When you run "locate.py", you will see windos as follow:

![image-20220103175207359](https://user-images.githubusercontent.com/76271045/147918727-ca84591e-eb9b-4801-b356-cc557e485aa0.png)




When you run "locateANDsegment.py", you will see results as follow:

![image-20220103175824434](https://user-images.githubusercontent.com/76271045/147918795-0c14d3c9-58df-4108-a20d-aaf1634fa3fc.png)

![image-20220103175839575](https://user-images.githubusercontent.com/76271045/147918814-f294b029-d142-40e0-a74d-9131c1add751.png)



<u>A character will appear every time you enter!</u>

Finally๏ผwe will see the windows of  liscense plate!

![image-20220103180053089](https://user-images.githubusercontent.com/76271045/147918831-e27bb3a2-f750-4248-8fde-36abc32f3797.png)




**Tips:**You can adjust the parameters to observe the positioning effect.



## Welfare

I integrated "segment.py" with "locate.py", that called "locateANDsegment.py".

At the same time,I encapsulated every step into a function for you to check!



## Write at the end

Since it is the first time for me to work on a project, I don't have much experience. If there is any unreasonable description, please correct me.
Thank you!!๐๐
