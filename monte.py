import math
import random

def dentro_circulo(e):
    x,y = e 
    a = 1/2
    b = 1/2
    p1 = (x-a)**2
    p2 = (y-b)**2
    ponto_imagem = math.sqrt(p1 + p2)

    dentro_do_circulo = ponto_imagem < 1/2
    if(dentro_do_circulo):
        return True
    else:
        return False


def adiciona_pontos_rand():
    x = random.random()
    y = random.random()
    return (x ,y)

qntd_chuts = 100000000

qntd_acerto=0
for go in range(qntd_chuts):
	chute = adiciona_pontos_rand()
	if dentro_circulo(chute):
		qntd_acerto = qntd_acerto + 1



print("o valor de py é {}".format(4*float(float(qntd_acerto)/float(qntd_chuts))))



    