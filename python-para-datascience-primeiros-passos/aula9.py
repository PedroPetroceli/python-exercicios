preco_produto1 = float(input('Preço do primeiro produto: '))
preco_produto2 = float(input('Preço do segundo produto: '))
preco_produto3 = float(input('Preço do terceiro produto: '))
mais_barato = preco_produto1
if preco_produto2 < mais_barato:
  mais_barato = preco_produto2
if preco_produto3 < mais_barato:
  mais_barato = preco_produto3

print(f'Indico esse produto {mais_barato}')