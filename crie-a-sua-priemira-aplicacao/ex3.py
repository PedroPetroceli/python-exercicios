usuario = 'pedro'
senha = 123
login = input('informe seu login: ')
password = int(input('informe sua senha: '))

if login == usuario and password == senha:
  print('login e password estão corretos')
else:
  print('login e password incorretos')  