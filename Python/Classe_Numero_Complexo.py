class NumeroComplexo:
    '''Classe para fazer operações de números complexos'''
    def __init__(self, a, b, c): #Método construtor de classe
        self.x = a
        self.y = b
        self.z = c
    def soma_complexo(self):
        soma = self.x + self.y + self.z
        return "A soma dos números reais é: " + str(soma)
    def subtracao_complexo(self):
        subtracao = self.x - self.y - self.z
        return "A subtração dos números reais é: " + str(subtracao)
    def multiplicacao_complexo(self):
        multiplicacao = self.x * self.y * self.z
        return "A soma dos números reais é: " + str(multiplicacao)
    def divisao_complexo(self):
        divisao = (self.x / self.y) / self.z
        return "A soma dos números reais é: " + str(divisao)

print("\nPROGRAMA PARA FAZER OPERAÇÕES BÁSICAS COM 3 NÚMEROS COMPLEXOS\n")
numr1 = float(input("Digite a parte real do primeiro número complexo:\n"))
numi1 = float(input("Digite a parte imaginária do primeiro número complexo:\n"))
numr2 = float(input("Digite a parte real do segundo número complexo:\n"))
numi2 = float(input("Digite a parte imaginária do segundo número complexo:\n"))
numr3 = float(input("Digite a parte real do terceiro número complexo:\n"))
numi3 = float(input("Digite a parte imaginária do terceiro número complexo:\n"))

num1 = complex(numr1,numi1)
num2 = complex(numr2,numi2)
num3 = complex(numr3,numi3)

print(f"\nPrimeiro número: {num1}")
print(f"Segundo número: {num2}")
print(f"Terceiro número: {num3}")

execucao = NumeroComplexo(num1,num2,num3)
ope = 0
while (ope < 1) or (ope > 4):
    ope = int(input("\nDigite qual operação deseja realizar com esses números:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n\n"))
match ope:
    case 1:
        resp = execucao.soma_complexo()
        print(resp)
    case 2:
        resp = execucao.subtracao_complexo()
        print(resp)
    case 3:
        resp = execucao.multiplicacao_complexo()
        print(resp)
    case 4:
        resp = execucao.divisao_complexo()
        print(resp)