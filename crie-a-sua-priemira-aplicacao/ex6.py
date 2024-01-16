"""
2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
"""
numeros = [1,2,3,4,5,6,7,8,9,10]
soma_impares = 0
for i in range(1, 11, 2):
  soma_impares += i
  print(soma_impares)

print()

for i in range(10, 0, -1):
  print(i)
  



