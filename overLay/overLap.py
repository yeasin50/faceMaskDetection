#!/usr/bin/env python
# coding: utf-8

# # <center>0verlay </center>
# Overlay need extra channel alpha 
#  

# Backgroung Image

# In[13]:


import cv2
import imutils
import numpy as np

# image = cv2.imread(r'images/_DSC0022.jpg') 
# target_img = imutils.resize(image, width=600)
# guy_img = cv2.imread(r'images/okleft.png')
# guy_img = imutils.resize(guy_img, width=200)

# a = np.where(guy_img > 0)
# b = np.where(target_img == 129)  # picked one of the channels in your image
# bbox_guy = np.min(a[0]), np.max(a[0]), np.min(a[1]), np.max(a[1])
# bbox_mask = np.min(b[0]), np.max(b[0]), np.min(b[1]), np.max(b[1])


# guy = guy_img[bbox_guy[0]:bbox_guy[1], bbox_guy[2]:bbox_guy[3],:]
# target = target_img[bbox_mask[0]:bbox_mask[1], bbox_mask[2]:bbox_mask[3],:]


# guy_h, guy_w, _ = guy.shape
# mask_h, mask_w, _ = target.shape
# fy = mask_h / guy_h
# fx = mask_w / guy_w
# scaled_guy = cv2.resize(guy, (0,0), fx=fx,fy=fy)


# for i, row in enumerate(range(bbox_mask[0], bbox_mask[1])):
#     for j, col in enumerate(range(bbox_mask[2], bbox_mask[3])):
#         target_img[row,col,:] = scaled_guy[i,j,:]

# cv2.imshow('Image', target_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Create extra 1 channel for overlay

# In[104]:



#base mode is created on w=600
# you may thinking about  x* 8//42 this type of operation, this thing made UI responsive to any images 
def drawEmoji(image, mode):
    #center 
    x, y = image.shape[0]//10 ,  image.shape[1]//10 
    
#     print(x, y)
    
    if mode: #happy
        borderColor =  (103, 255, 0)
        eyeRadius = x* 8//42
        mouthColor = (0,255,255)
        eyeColor= (17, 13, 255)
        
        axes = (x*30//42, x*30//42)
        angel = 0
        startAngel = 10
        endAngel = 170
        thickness = x*5 // 42
        
         #face border
        cv2.circle(image, (x, y), x, borderColor)
        
        cv2.ellipse(image, (x, y), axes, angel, startAngel, endAngel, mouthColor, thickness)
        cv2.circle(image, (x- x*15//42, y- x*10//42), eyeRadius, eyeColor , -1)
        cv2.circle(image, (x+ x*15//42, y-x*10//42), eyeRadius, eyeColor , -1)
    
    else: #Sad
        borderColor = (255,131,13)
        eyeRadius = x * 5 // 42 
        eyeColor = (0, 255, 239)
        mouthColor= (255, 0, 119)
        thickness = x *5 //42
        axes = (x*30//42, x*30//42)
        angel = 0

        #face border
        cv2.circle(image, (x, y), x, borderColor)
        
        #sad
        cv2.ellipse(image, (x, y+x), axes, angel, 220, 320, (0, 0, 123), thickness)
        cv2.circle(image, (x- x*15//42, y-x*10//42), eyeRadius, eyeColor , -1)
        cv2.circle(image, (x+ x*15//42, y-x*10//42), eyeRadius, eyeColor , -1)

    return image

# In[105]:



# bgImage = cv2.imread(r'images/_DSC0022.jpg', -1)
# bgImage  = imutils.resize(image, width=640)
# # bgImage = cv2.cvtColor(bgImage, cv2.COLOR_BGR2BGRA)
# print(bgImage.shape)

# bgSad = drawEmoji(bgImage.copy(), False)
# cv2.imshow("BGimage2", bgSad)


# bgImage = drawEmoji(bgImage.copy(), True)
# cv2.imshow("BGimageHappy", bgImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# if you have saing issue remove alpha channel just before saving 
# cv2.cvtColor(bgImage, cv2.COLOR_BGRA2BGR)
# 

# In[ ]:




