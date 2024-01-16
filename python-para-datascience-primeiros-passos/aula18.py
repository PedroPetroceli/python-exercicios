inicio = int(input('Primeiro numero inteiro: '))
fim = int(input('Segundo numero inteiro: '))

if inicio < fim:
  for i in range(inicio + 1, fim):
    print(i)
elif inicio > fim:
  for i in range(fim + 1, inicio):
    print(i)
else:
  print('Os números são iguais.')
