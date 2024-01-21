#Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
#Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
#Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
#Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

class Livro:
  def __init__(self, titulo, autor, ano_publicacao):
    self.titulo = titulo
    self.autor = autor
    self.ano_puclicacao = ano_publicacao
    self.disponivel = True
  def __str__(self):
    return f'{self.titulo}, {self.autor}, {self.ano_puclicacao}'
  def emprestar(self):
    self.disponivel = False
  def verificar_disponibilidade(ano):
    livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
    return livros_disponiveis

livro1 = Livro('Percy Jackson', 'Aribaba', 2010)  
livro2 = Livro('Ratatulie', 'Bernardo', 2013)
livro3 = Livro('Babacao', 'Minister', 1996)
livro3.emprestar()
print(f'{livro1} | {livro2}')
print(f'Livro {livro3}, disponibilidade: {livro3.disponivel}')
Livro.livros = [livro1, livro2, livro3]