class Pessoa(object):
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
    def get_nome(self):
        return self.nome
    def set_nome(self, n):
        self.nome = n
    def get_ano(self):
        return self.ano
    def set_ano(self, a):
        self.ano = a

pessoa = Pessoa("Maria", 1990)
print(f"\nMeu nome é {pessoa.get_nome()} e eu nasci em {pessoa.get_ano()}")
n = input("\nDigite um novo nome: ")
pessoa.set_nome(n)
a = int(input("\nDigite um novo ano: "))
pessoa.set_ano(a)
print(f"\nMeu novo nome é {pessoa.get_nome()} e agora eu nasci em {pessoa.get_ano()}")