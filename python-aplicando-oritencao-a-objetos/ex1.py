# código omitido
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
#Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = 'Italiana'
#Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
nome_do_resturante = restaurante_praca.nome
#Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo == True:
  print('resturante ativo')
else: 
   print('não está ativo')
#Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria
# Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'
# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
resturante_pizza = Restaurante()
resturante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
   print('Categoria Fast Food')
else:
   print('Categoria incorreta')
#Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.categoria = True
#Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')

