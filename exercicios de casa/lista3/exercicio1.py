import random
import math

numeros = [3,24,4,12,5,2,1,9,0,1]

alvo = 9

aux=[]

for i in range(1, len(numeros) + 1):
    j = 0
    c = math.comb(len(numeros),i)
    while j <= c:
        valor = random.sample(numeros,i)
        if valor not in aux:
            aux.append(valor)
            j += 1
            soma = 0
            for num in valor:
                soma += num
            if soma == alvo:
                print(valor)
        else:
            continue

# nao esta completo esse codigo