class Musica:
    def __init__ (self, nome, artista, duracao):
      self.nome = nome
      self.artista = artista
      self.duracao = duracao
    def __str__ (self):
       return f'{self.nome}| {self.artista} | {self.duracao}'  

print(Musica('Anjos', 'Banda Eva', '50 minutos'))      
