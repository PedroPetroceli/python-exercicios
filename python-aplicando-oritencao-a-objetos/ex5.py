# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
#Crie uma instância da classe e imprima o valor da propriedade titular.
#Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
#Crie um método de classe para a conta ClienteBanco.


class ContaBancaria:
  def __init__(self, titular, saldo):
    self.titular = titular
    self.saldo = saldo
    self._ativo = False
  def __str__(self):
    return f'Titular da conta: {self.titular}, Saldo de: {self.saldo}'  
  @classmethod
  def ativar_conta(cls, conta):
    conta._ativo = True
  
conta1 = ContaBancaria('Pedro', 1000,)
conta2 = ContaBancaria('Juliana', 2000)  
print(conta1, conta2)
conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
conta4 = ContaBancariaPythonica('Bernardo', 5000)
print(f'Titular da conta 4: {conta4.titular}')

class ClienteBanco:
   def __init__(self, nome, idade, profissao, cor, banco):
      self.nome = nome
      self.idade = idade
      self.profissao = profissao
      self.cor = cor
      self.banco = banco
      self._ativo = False
   def __str__(self):
      return f'Cliente: {self.nome}, idade: {self.idade}, Profissao:{self.profissao}, Cor:{self.cor}, Banco:{self.banco}'
   @classmethod
   def ativar_conta(cls, conta):
    conta._ativo = True

cliente1 = ClienteBanco('Pedro', 27, 'Professor', 'Branco', 'Santander')
cliente2 = ClienteBanco('Juliana', 30, 'Recursos Humanos', 'Preta', 'Nubank')
cliente3 = ClienteBanco('Bernardo', 4, 'Vagabundo', 'Branquissimo', 'Picpay')
  
