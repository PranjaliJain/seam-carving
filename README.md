# Seam Carving
Implementation of "Seam Carving for Content-Aware Image Resizing", SIGGRAPH 2007

As part of our (Naman Jain and Pranjali Jain) Computer Vision Project


To access the code for changing the size of the image:

```
 import SeamCarving
 import cv2

 img = cv2.imread("test_image.png")
 img_new = SeamCarving.perform_change(img, (desired_width, desired_height))
 ```


To access the code for changing the removing an object:

```
 import SeamCarving
 import cv2

 img = cv2.imread("test_image.png")
 img_new = SeamCarving.object_removal(img, masking_box)
```

masking_box refers to a list of corners required to enclose the object to be removed. 
```
masking_box = [up_row, down_row, left_col, right_col]
```
