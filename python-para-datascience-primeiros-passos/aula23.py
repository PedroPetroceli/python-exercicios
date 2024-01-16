#coletamos o número
num = int(input('Insira um número inteiro: '))

# números inteiros iguais ou abaixo de 1 não consideramos primos
if num > 1:
    for i in range(2, num):
        # verificamos todos os restos de divisões entre todos os números abaixo de num
        # se algum resto for 0, então ele é divisível por outro número além dele e 1
        if (num % i) == 0:
            print(f'{num} não é um número primo')
            break
        else:
            print(f'{num} é um número primo')
else:
    print(f'{num} não é um número primo')
