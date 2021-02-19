#!/usr/bin/env python
# coding: utf-8
## testCases

# # <center>0verlay </center>
# Overlay need extra channel alpha 
#  

# Backgroung Image

# In[180]:


import cv2
import imutils
import numpy as np

image = cv2.imread(r'images/_DSC0022.jpg') 
bgImage = imutils.resize(image, width=600)
bgImage = cv2.cvtColor(bgImage, cv2.COLOR_BGR2BGRA)
frame_h, frame_w, frame_ch = bgImage.shape
print(bgImage.shape)


# Create extra 1 channel for overlay

# In[181]:


image = cv2.imread(r'images/colorChart.jpg', -1)
watermark  = imutils.resize(image, width=140)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)
print(watermark.shape)


# In[168]:


overlay = np.ones((frame_h, frame_w, 4), dtype="uint8")
waterMark_h, waterMark_w, waterMark_ch = watermark.shape

for i in range(waterMark_h):
    for j in range(waterMark_w):
        #png always has alpha 
        if watermark[i, j][3]!=0:
            overlay[i, j] = watermark[i,j]

cv2.addWeighted(overlay, 1, bgImage, .5, 0,bgImage)
bgImage = cv2.cvtColor(bgImage, cv2.COLOR_BGRA2BGR)
cv2.imshow("BGimage2", bgImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


# if you have saing issue remove alpha channel just before saving 
# cv2.cvtColor(bgImage, cv2.COLOR_BGRA2BGR)
# 

# In[ ]:




