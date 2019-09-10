import numpy as np
import cv2
from matplotlib import pyplot as plt


height = 300
width =200

#abrindo uma imagem e mostrando as propriedadeds dela
#tirar o pedaco que manipula
# vetor de dados inteiro 
blank_image = np.zeros((height,width,3), np.uint8) # estrutura, esqueleto
# blank_image[:,0:width//2] = (255,0,0)      # (B, G, R)
# blank_image[:,width//2:width] = (0,255,0)


blank_image[0:height//2, 0:width] = (150,200,80) #whtie slice
blank_image[height//2:height, 0:width] = (0,0,0) #preto slice




plt.imshow(blank_image, 'gray')
plt.show()
#histrogram array qye sera contado, a quantidade de bins, a variaçao dos bins

plt.hist(blank_image.ravel(),256,[0,256])
plt.show()

# faca uma imagem ..... 
# color_image = np.zeros((height,width,3), np.uint8)


r = blank_image.copy()
g = blank_image.copy()
b = blank_image.copy()


b[:,:,1] = 0
b[:,:,2] = 0





cv2.imshow("r",b)

g[:,:,0]= 0
g[:,:,2] = 0
cv2.imshow("g",g)
r[:,:,0]= 0
r[:,:,1] = 0
cv2.imshow("g",r)

cv2.waitKey(0)



































