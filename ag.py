import random
import numpy as np
from colorutils import Color

#[random.randint(0, 255) for i in range(tam_rgb)]
#cor = hex([random.randint(0, 255) for i in range(tam_rgb)])

arrayPopulacao = list()
geracao = 1
terminar = 0
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def gerarPopulacaoRGB():
    for i in range(0,4):
        color = "%06x" % random.randint(0, 0xFFFFFF)
        arrayPopulacao.append(hex_to_rgb((color)))

def fitness():
    c1 = Color(arrayPopulacao[0])
    c2 = Color(arrayPopulacao[1])
    c3 = Color(arrayPopulacao[2])
    c4 = Color(arrayPopulacao[3])
    c5 = Color((70, 70, 70))

    if(c4.rgb <= c5.rgb and c3.rgb <= c5.rgb and c2.rgb <= c5.rgb and c1.rgb <= c5.rgb):
        print("Objetivo alcançado")
        return "parar"
    else:
        print('{}°geração'.format(geracao))
        arrayPopulacao.sort() 
        return "naoparar" 
      
def crossover():
    c1 = Color(arrayPopulacao[2]) - Color(arrayPopulacao[0])
    c2 = Color(arrayPopulacao[3]) - Color(arrayPopulacao[0])
    c3 = Color(arrayPopulacao[2]) - Color(arrayPopulacao[1])
    c4 = Color(arrayPopulacao[3]) - Color(arrayPopulacao[1])

    arrayPopulacao.clear()

    arrayPopulacao.append(hex_to_rgb(c1.hex))
    arrayPopulacao.append(hex_to_rgb(c2.hex))
    arrayPopulacao.append(hex_to_rgb(c3.hex))
    arrayPopulacao.append(hex_to_rgb(c4.hex))


def mutacao():
    quant = random.randint(0,50)
    individuo = random.randint(0,3)
    operacao = random.randint(0,1)
    if(operacao == 1):
        c1 = Color(arrayPopulacao[individuo])
        selec = arrayPopulacao[individuo]
        arrayPopulacao.remove(selec)
        if(c1.green + quant > 255):
            new_rgb = (selec[0], 255, selec[2])
        else:
            new_rgb = (selec[0], c1.green + quant, selec[2])
        arrayPopulacao.insert(individuo, new_rgb)
    else:
        c1 = Color(arrayPopulacao[individuo])
        selec = arrayPopulacao[individuo]
        arrayPopulacao.remove(selec)
        if(c1.green - quant < 0):
            new_rgb = (selec[0], 0, selec[2])
        else:
            new_rgb = (selec[0], c1.green - quant, selec[2])
        arrayPopulacao.insert(individuo, new_rgb)
       
        

    


gerarPopulacaoRGB()
print(arrayPopulacao)

while terminar == 0:
    geracao += 1
    if(fitness() == "parar" or geracao > 15 ):
        terminar += 1
    else:
        crossover()
        mutacao()
        print(arrayPopulacao)
    



