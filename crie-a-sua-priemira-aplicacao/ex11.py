"""
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

2 - Utilizando o dicionário criado no item 1:
Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
"""

info = {'nome': 'Pedro', 'idade': 27, 'cidade': 'Rio de Janeiro'}
info['idade'] = 28 
info['profissao'] = 'Dev'
del info['cidade']
print(info)