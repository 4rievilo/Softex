class String(object):
    def __init__(self, palavra):
        self.palavra = palavra
    def Maiuscula(self):
        print(self.palavra.upper())
    def Menuscula(self):
        print(self.palavra.lower())
    def Tamanho(self):
        print(len(self.palavra))

frase = String("O Rato Roeu a Roupa do Rei de Roma")
frase.Maiuscula()
frase.Menuscula()
frase.Tamanho()