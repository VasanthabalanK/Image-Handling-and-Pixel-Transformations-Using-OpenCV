#!/usr/bin/env python
# coding: utf-8

# ### EXP-1 Image-Handling-and-Pixel-Transformations-Using-OpenCV
# ### NAME: VASANTHABALAN K
# ### REG.NO: 212224230296    

# In[ ]:


import cv2
import matplotlib.pyplot as plt


# In[149]:


img = cv2.imread('images.jpg', cv2.IMREAD_COLOR)


# In[150]:


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[151]:


plt.imshow(img_rgb, cmap='viridis')  
plt.title("Original Image")
plt.axis('off')  
plt.show()


# In[152]:


image = cv2.imread('images.jpg') 


# In[153]:


img_rgb.shape


# In[154]:


line_img = cv2.line(img_rgb, (0, 0), (768, 600), (255, 0, 0), 2)


# In[155]:


plt.imshow(line_img, cmap='viridis')  
plt.title("Image with Line")
plt.axis('off')  
plt.show()


# In[156]:


image = cv2.imread('images.jpg') 

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[157]:


img_rgb.shape


# In[158]:


circle_img = cv2.circle(img_rgb,(400,300),150,(255,0,0),10) 


# In[159]:


plt.imshow(circle_img, cmap='viridis')  
plt.title("Image with Circle")
plt.axis('off')  
plt.show()


# In[160]:


image = cv2.imread('images.jpg') 

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[161]:


img.shape


# In[162]:


rectangle_img = cv2.rectangle(img_rgb, (0, 0), (739, 415), (0, 0, 255), 10) 


# In[163]:


plt.imshow(rectangle_img, cmap='viridis')  
plt.title("Image with Rectangle")
plt.axis('off')  
plt.show()


# In[164]:


image = cv2.imread('images.jpg') 

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[165]:


text_img = cv2.putText(img_rgb, "OpenCV Drawing", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 10) 


# In[166]:


plt.imshow(text_img, cmap='viridis')  
plt.title("Image with Text")
plt.axis('off')  
plt.show()


# In[167]:


image = cv2.imread('images.jpg') 


# In[168]:


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[169]:


plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis("off")


# In[170]:


# Convert RGB to HSV
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)


# In[171]:


# HSV Image
plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")


# In[172]:


image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)


# In[173]:


plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")


# In[174]:


image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)


# In[175]:


plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")


# In[176]:


image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)


# In[177]:


plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB Image")
plt.axis("off")


# In[178]:


image[200:500, 200:500] = [255, 255, 255] 


# In[179]:


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[180]:


plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()


# In[181]:


image = cv2.imread('images.jpg') 


# In[182]:


# Resize the image to half its size
resized_image = cv2.resize(image, (768 // 2, 600 // 2))  # (new_width, new_height)


# In[183]:


# Convert BGR to RGB for displaying with Matplotlib
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)


# In[184]:


resized_image_rgb.shape


# In[185]:


plt.imshow(resized_image_rgb)
plt.title("Resized Image (Half Size)")
plt.axis("off")
plt.show()


# In[186]:


roi = image[50:350, 50:350]
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
plt.imshow(roi_rgb)
plt.title("Cropped Region of Interest (ROI)")
plt.axis("off")
plt.show()


# In[187]:


flipped_horizontally = cv2.flip(image, 1)
# Convert BGR to RGB for displaying with Matplotlib
flipped_horizontally_rgb = cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB)
plt.imshow(flipped_horizontally_rgb)
plt.title("Flipped Horizontally")
plt.axis("off")


# In[188]:


flipped_vertically = cv2.flip(image, 0)
flipped_vertically_rgb = cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB)
plt.imshow(flipped_vertically_rgb)
plt.title("Flipped Vertically")
plt.axis("off")


# In[ ]:




