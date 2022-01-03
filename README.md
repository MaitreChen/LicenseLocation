# LicenseLocation

Hi,everyone!
This is my first project!
Actually,this is an assignment from my digital image processing experiment class.
Through thinking about algorithm ideas and the process of constantly adjusting parameters by myself, I successfully completed this project.


You can clone this project to local and run it.
Now,here is something to tell you:

**First**,the "test.jpg" is the original image,and the "img.jpg" is a picture that i preprocessed.Among them,I used OTSU and morphological operations.

**Second**,when you run "segment.py",you can see two windows as follow，also every character will be saved in your directory.

![image](https://user-images.githubusercontent.com/76271045/147907507-0ea9bad0-ca20-499a-acd5-294fcc067569.png)
![image](https://user-images.githubusercontent.com/76271045/147907606-543f6e1b-bd84-49d4-863b-42b4b9b14efa.png)

The second window shows the characters of the license plate segmentation. If you want to  display each character separately, you can modify my code to achieve.

**Thirdly**, I will describe the algorithm idea.

1.Image preprocessing,including gray conversion, threshold processing and orphological operation.(Of course, I also made a clever treatment to manually remove information that has nothing to do with characters.If there is no such operation, perhaps all the subsequent efforts will be wasted)
2.Traverse the picture by column, if the sum of a certain column of pixels is zero, then it can be used as the position of the dividing line.
3.Since only one dividing line needs to be located between the characters, the difference method is used here to remove the continuous lines: all continuous values with a difference less than D are set to the first value in the range, and then the duplicates are removed.
4.Through the third step, we can successfully cut the characters, but there is an annoying separator. I used a special judgment. Traverse the lines, extract the ROI of each part, display and save characters through formatting control.

Last, since it is the first time for me to work on a project, I don't have much experience. If there is any unreasonable description, please correct me.
Thank you!!
