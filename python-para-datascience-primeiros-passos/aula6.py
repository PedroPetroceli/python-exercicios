percentual = float(input('Qual o percentual de crescimento de produção: '))
if percentual > 0:
  print(f'A porcentagem de {percentual}% foi positiva!')
elif percentual == 0:
  print(f'A porcentagem de {percentual}% foi estável!')
else:
  print(f'A procentagem de {percentual}% foi negativa!')