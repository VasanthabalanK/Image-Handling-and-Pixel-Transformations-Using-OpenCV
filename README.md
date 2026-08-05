# Image-Handling-and-Pixel-Transformations-Using-OpenCV

# AIM:
Write a Python program using OpenCV that performs the following tasks:

Read and Display an Image.
Adjust the brightness of an image.
Modify the image contrast.
Generate a third image using bitwise operations.
# Software Required:
Anaconda - Python 3.7
Jupyter Notebook (for interactive development and execution)
# Algorithm:
# Step 1:
Load an image from your local directory and display it.

# Step 2:
Create a matrix of ones (with data type float64) to adjust brightness.

# Step 3:
Create brighter and darker images by adding and subtracting the matrix from the original image.
Display the original, brighter, and darker images.

# Step 4:
Modify the image contrast by creating two higher contrast images using scaling factors of 1.1 and 1.2 (without overflow fix).
Display the original, lower contrast, and higher contrast images.

# Step 5:
Split the image (boy.jpg) into B, G, R components and display the channels

# Program Developed By:
### Name:Vasanthabalan K
### Reg.No:212224230296
# Step 1: Read and Display Image
```
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('vr46.png', cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb, cmap='viridis')  
plt.title("Original Image")
plt.axis('off')  
plt.show()
```
# Step 2: Draw a Line
```
line_img = cv2.line(img_rgb, (0, 0), (768, 600), (255, 0, 0), 2)
plt.imshow(line_img, cmap='viridis')  
plt.title("Image with Line")
plt.axis('off')  
plt.show()
```
# Step 3: Draw a Circle
```
circle_img = cv2.circle(img_rgb,(400,300),150,(255,0,0),10)
plt.imshow(circle_img, cmap='viridis')  
plt.title("Image with Circle")
plt.axis('off')  
plt.show()
```
# Step 4: Draw a Rectangle
```
rectangle_img = cv2.rectangle(img_rgb, (0, 0), (768, 600), (0, 0, 255), 10)
plt.imshow(rectangle_img, cmap='viridis')  
plt.title("Image with Rectangle")
plt.axis('off')  
plt.show()
```
# Step 5: Add Text
```
text_img = cv2.putText(img_rgb, "OpenCV Drawing", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 10)
plt.imshow(text_img, cmap='viridis')  
plt.title("Image with Text")
plt.axis('off')  
plt.show()
```
# Step 6: Convert RGB to HSV
```
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")
```
# Step 7: Convert RGB to Gray
```
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
```
# Step 8: Convert RGB to YCrCb
```
image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)
plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")
```
# Step 9: Convert HSV back to RGB
```
image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)
plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB Image")
plt.axis("off")
```
# Step 10: Modify Pixel Block
```
image[200:500, 200:500] = [255, 255, 255]
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()
```
# Step 11: Resize Image
```
resized_image = cv2.resize(image, (768 // 2, 600 // 2))
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
plt.imshow(resized_image_rgb)
plt.title("Resized Image (Half Size)")
plt.axis("off")
plt.show()
```
Step 12: Crop ROI
```
roi = image[50:350, 50:350]
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
plt.imshow(roi_rgb)
plt.title("Cropped Region of Interest (ROI)")
plt.axis("off")
plt.show()
```
# Step 13: Flip Horizontally
```
image = cv2.imread('vr46.png')
flipped_horizontally = cv2.flip(image, 1)
flipped_horizontally_rgb = cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB)
plt.imshow(flipped_horizontally_rgb)
plt.title("Flipped Horizontally")
plt.axis("off")
```
# Step 14: Flip Vertically
```
flipped_vertically = cv2.flip(image, 0)
flipped_vertically_rgb = cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB)
plt.imshow(flipped_vertically_rgb)
plt.title("Flipped Vertically")
plt.axis("off")
```
# Step 15: Save Final Image
```
cv2.imwrite(
"final_output.jpg",
flipped_horizontally
)**
```
# output:
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/a81604c2-c8e3-43e0-9770-3d40256441ca" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/826e6747-4d89-4b25-893c-ac5bb982cb1d" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/ea88f7a0-74ce-4e35-9ee2-5162350aad5f" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/8330950e-cbea-4cbb-a35e-38306d384f0c" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/503060f0-09fc-40e2-aec6-d5fa33791639" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/0f74bd48-1894-43dd-be3e-a1817d07488e" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/d115630e-c6d7-42e0-89b0-66e9bdc12ff8" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/3b11f143-69d0-4669-aff0-443da75befd0" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/2ab40d8a-e949-47ad-9d10-bc640a244f4d" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/f084a031-f891-4ef6-8252-061bf70f52fd" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/16a57cfd-013e-4bc2-b999-3d170787dabc" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/a1a021f9-1262-4590-9dd9-46ac49e7931e" />
<img width="389" height="409" alt="image" src="https://github.com/user-attachments/assets/8bf60f2d-1015-4d3b-957d-a899c0d4c470" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/2a4f7638-db93-4692-a686-ccee9685711c" />
<img width="493" height="409" alt="image" src="https://github.com/user-attachments/assets/01643da4-344d-49be-bbea-01e1d5a305bb" />

# Result:

Thus, the images were read, displayed, brightness and contrast adjustments were made, and bitwise operations were performed successfully using the Python program.
