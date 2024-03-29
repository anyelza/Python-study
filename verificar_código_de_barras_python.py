# -*- coding: utf-8 -*-
"""Verificar-Código-de-Barras-Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iiXcY5YP79TeJ-EKhNXIN1Ota8KiFDVB

# Código: Código de barras

Autoria: Anyele Seifert
"""

from math import floor
codigo = str(input('Digite o código de barras: '))
#print(f'\nO código de barras é {codigo}')

# Remover caracteres especiais para o código
codigo = ''.join(char for char in codigo if char.isdigit())

resultado = 0

# Executando o loop até a posição 12 da string
for i in range(min(len(codigo), 12)):
  digito = int(codigo[i])
  if i % 2 == 0 :
    resultado += digito*1
  else:
    resultado += digito*3

resultadoModificado = resultado /10
resultadoarredondado = floor(resultadoModificado)
resultadosomado = resultadoarredondado + 1
resultadomultiplicado = resultadosomado * 10
resultadoFinal = resultadomultiplicado - resultado
print(f'\nO dígito verificador obtido pela análise é {resultadoFinal}')

digitoVerificador = int(codigo[12])
if resultadoFinal == digitoVerificador:
  print('Código de barras está Ok')
else:
  print('Código de barras está inválido')