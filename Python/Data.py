def id(a):
    if (a>=1922 and a<=2021):
        return (2022 - a)




nome = input("\nDigite seu nome completo:\n")
ano=1
while ano>2021 or ano<1922:
    try:
        ano = int(input("Digite seu ano de nascimento:\n"))
        if ano>2021 or ano<1922:
            raise Exception("Digite um número entre 1922 e 2021.\n")
    except Exception as erro:
        print("\nCódigo com erro.")
        print(f"{erro}\n")
        ano=1
idade = id(ano)
print(f"{nome} em 2022 terá {idade} anos.\n")        