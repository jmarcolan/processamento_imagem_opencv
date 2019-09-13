
# IMPORTANTE AS BIBLIOTECAS
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ABRINDO A IMAGEM 
img = cv2.imread('./p1/rgb.png')
height, width = img.shape[:2]

# segmentando os cananeis
# segmenta 
b,g,r = cv2.split(img)
img2 =cv2.merge([r,g,b])
zero_only_image = np.zeros((height,width,1), np.uint8) # estrutura, esqueleto

# uni

img_r = cv2.merge([r, r, r])
img_g = cv2.merge([g, g, g,])
img_b = cv2.merge([b, b, b])


plt.hist(r.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
# plt.subplot(121);plt.imshow(img) # expects distorted color
# plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr original image',img) # expects true color
# cv2.imshow('rgb image',img2) # expects distorted color
cv2.imshow('red chanels image',img_r) # expects true color
cv2.imshow('green chanels image',img_g) # expects true color
cv2.imshow('blue chanels image',img_b) # expects true color
# cv2.imshow('rgb image',img2) # expects distorted color


cv2.waitKey(0)
cv2.destroyAllWindows()
