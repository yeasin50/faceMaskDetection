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


# filled image  (main img, overlayImg, possition(x,y))
def overlay100(l_img, s_img, offset):

    (x_offset,y_offset)= offset

    s_img = cv2.cvtColor(s_img, cv2.COLOR_BGR2BGRA)

    y1, y2 = y_offset, y_offset + s_img.shape[0]
    x1, x2 = x_offset, x_offset + s_img.shape[1]

    alpha_s = s_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
                                  alpha_l * l_img[y1:y2, x1:x2, c])
        
    return l_img