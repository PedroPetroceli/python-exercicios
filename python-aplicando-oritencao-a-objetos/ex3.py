"""
Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
"""
class Carro:
  def __init__ (self, modelo, cor, ano = 0):
    self.modelo = modelo
    self.cor = cor 
    self.ano = ano
  def __str__ (self):
    return f'Modelo = {self.modelo}, Cor = {self.cor}, Ano = {self.ano}'

print(Carro('Peugeot', 'Preto', 96))  

"""
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
"""
class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
      self.nome = nome
      self.categoria = categoria
      self.ativo = ativo
restaurante_exemplo = Restaurante(nome='Comida Boa', categoria='Gourmet', ativo=True)        

"""
Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
"""
