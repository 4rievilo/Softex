class acessoNetflix (object):
    def __init__(self, nome, conta, num):
        self.conta = conta
        self.nome = nome
        self.num = num

    def acessos(self):
        if (self.conta == 1):
            self.num = self.num+1
            print(f"\n{self.nome} já acessou na Netflix {self.num}x esse mês.")
            return self.num
        elif (self.conta == 2):
            self.num = self.num+1
            print(f"\n{self.nome} já acessou na Netflix {self.num}x esse mês.")
            return self.num
        elif (self.conta == 3):
            self.num = self.num+1
            print(f"\n{self.nome} já acessou na Netflix {self.num}x esse mês.")
            return self.num
        else:
            print("\nConta Inválida!")


k = [0, 0, 0]
while True:
    while True:
        maria = acessoNetflix("Maria", 1, k[0])
        paulo = acessoNetflix("Paulo", 2, k[1])
        jose = acessoNetflix("José", 3, k[2])
        try:
            print("\nVocê deseja acessar a Netflix com que conta?\n")
            c = int(input(" 1. Maria\n 2. Paulo\n 3. José\nNº: "))
            if (c == 1):
                k[0] = maria.acessos()
            elif (c == 2):
                k[1] = paulo.acessos()
            elif (c == 3):
                k[2] = jose.acessos()
            else:
                raise Exception()
            break
        except Exception as err:
            print("\nDigite apenas números entre 1 e 3.")
    a = input(
        "\nPara fazer um novo acesso, digite 's'. Para sair, pressione qualquer outra tecla.\nInsira: ")
    if (a != "s"):
        break
