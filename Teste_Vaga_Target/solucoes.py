# 1) 

# Resposta: Soma = 91

# 2) Fibonacci 

import math

def quadradoPerfeito(x):
    sqr = int(math.sqrt(x))
    return sqr * sqr == x

def isFibo(n):
    return quadradoPerfeito(5*n*n + 4) or quadradoPerfeito(5*n*n - 4)

n = int(input('Digite um número: '))

if isFibo(n):
    print(f'O número {n} é um Fibonacci.')
else:
    print(f'O número {n} não é um Fibonacci.')

# 3) Sequência Lógica

# a) 1,3,5,7,9 
# b) 2,4,8,16,32,64,128 
# c) 0,1,4,9,16,25,36,49
# d) 4,16,36,64,100
# e) 1,1,2,3,5,8,13,21
# f) 2,10,12,16,17,18,19,20

# 4) Independentemente da velocidade ou número de pedagios, quando os veiculos se encontrarem, 
# a distância deles em relação à Ribeirão Preto será a mesma. Ex: Se eles se encontrarem no km 50, 
# a distancia sera 50. Se eles se encontrarem no km 25, a distancia será 75. e vice versa.Pois estão 
# viajando em sentidos opostos, só haveria diferenciação se eles estivesssem viajando no mesmo sentido.

# inversor de Strings
texto = str(input('Digite uma frase: ')).split(None)
i = len(texto[0])

while i > 0:
    print(texto[0][i-1], end='')
    i -= 1
