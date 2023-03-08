
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




# 3)

import json
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

# Ler o arquivo JSON ou XML com os dados de faturamento
with open("dados_faturamento.json") as f:
    dados_faturamento = json.load(f)

# ou, se os dados estão em um arquivo XML:
# tree = ET.parse('dados_faturamento.xml')
# root = tree.getroot()
# dados_faturamento = [float(child.text) for child in root]

# Obter os valores de faturamento para cada dia útil do mês
faturamento_dia_util = []
data = datetime.today().replace(day=1)
mes_atual = data.month
while data.month == mes_atual:
    if data.weekday() < 5:  # Ignorar finais de semana
        faturamento = dados_faturamento[data.day-1]  # O índice do vetor começa em 0
        faturamento_dia_util.append(faturamento)
    data += timedelta(days=1)

# Calcular o menor valor, o maior valor e a média do faturamento diário
menor_valor = min(faturamento_dia_util)
maior_valor = max(faturamento_dia_util)
media_mensal = sum(faturamento_dia_util) / len(faturamento_dia_util)

# Contar o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(faturamento > media_mensal for faturamento in faturamento_dia_util)

# Imprimir os resultados
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento diário acima da média mensal:", dias_acima_da_media)



# 4) 
fatMensal = {"SP":67836.43,"RJ":36678.66,"MG":29229.88,"ES":27165.48,"OUTROS":19849.53}

total = sum(fatMensal.values())
for k, v in fatMensal.items():
    print(f'{k} tem {(v/total)*100:.1f}% sobre o valor total de faturamento mensal.')



# 5) inversor de Strings
texto = str(input('Digite uma frase: ')).split(None)
i = len(texto[0])

while i > 0:
    print(texto[0][i-1], end='')
    i -= 1
