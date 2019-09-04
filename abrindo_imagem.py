import numpy as np
import cv2
from matplotlib import pyplot as plt


# https://docs.opencv.org/3.2.0/d0/d86/tutorial_py_image_arithmetics.html
# rastreamento do animal na area.

# o que e uma image
# visuzliando uma imagem
# criando uma imagem 
# mostrando a imagem 
height = 300
width =200
# vetor de dados inteiro 
blank_image = np.zeros((height,width,3), np.uint8)
# blank_image[:,0:width//2] = (255,0,0)      # (B, G, R)
# blank_image[:,width//2:width] = (0,255,0)


blank_image[0:height//2, 0:width] = (255,255,255) #whtie
blank_image[height//2:height, 0:width] = (0,0,0) #whtie

color_image = np.zeros((height,width,3), np.uint8)

color_image[:, :] = (255,0,0) # red

dst = cv2.addWeighted(blank_image,0.7,color_image,0.3,0)

plt.imshow(dst, 'gray')
plt.show()


# adicionando elementos
def myfunc(r):
    return (230,230,230)


result = np.array(list(map(myfunc, dst)))


plt.imshow(result, 'gray')
plt.show()








plt.imshow(blank_image, 'gray')
plt.show()


# primeiro passo (toda a validação vem da vizualização)
    # io dos arquivos.
    # lendo e desenhando (inspecionando vizualmente)

# segundo desenhando o histograma
    # calculand o histograma.
    # imagem são compostas de 3 cores (r,g,b)



# aplicando mascaras



# aplicando mascaras





# desenhando usando o python




# Load an color image in grayscale
img = cv2.imread('messi5.jpg',0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])


mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)


# histograma de uma imagem colorida.




plt.hist(img.ravel(),256,[0,256])
plt.show()

plt.imshow(img, 'gray')
plt.show()



# filtros




# mostrando imagem
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# desenhando o resultado