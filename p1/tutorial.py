import cv2
import numpy as np
import matplotlib.pyplot as plt


# ocntruir uma imagem

# o que é uma imagme 
# como abrir e como vizualizar uma imagem
# abrir e vizualizações de imagem 

height = 300
width =300
# vetor de dados inteiro 
# uint8 Unsigned integer (0 to 255)
img = np.zeros((height,width,3), np.uint8) # estrutura, esqueleto
# b g  r
img[:, 0:100] = (0,0,255) #whtie slice
img[:, 100:200] = (0,255,0) #whtie slice
img[:, 200:300] = (255,0,0) #whtie slice

# vizualizar uma imagem 
cv2.imshow('image original', img) # expects true color
plt.show()
cv2.waitKey(0)







# acesar pixeis (slice)
canal_b = img[:,:,0]
img_b = cv2.merge([canal_b,canal_b,canal_b])
cv2.imshow('image blue', img_b) # expects true color

cv2.waitKey(0)



# olhar o histograma da imagem 
plt.hist(img.ravel(),256,[0,256])
plt.show()

# cv2.imshow('rgb image',img2) # expects distorted color





# 


# # exercicio aqui é abrir a imagme do mario e construir uma imagem somento com o canal vermelho.
# # abrir uma imagem
# # plotar o histograma de cada um dos canais.
# img = cv2.imread('./p1/rgb.png')
# # pegar a altura e a largura.
# height, width = img.shape[:2]



cv2.destroyAllWindows()