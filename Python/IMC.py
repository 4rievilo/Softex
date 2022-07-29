def imc (peso, altura):
    return peso/(altura*altura)

p = float(input("\nInsira seu peso:\n"))
a = float(input("\nInsira sua altura:\n"))
imc = imc(p,a)
print(f"Seu IMC é: {imc:.2f}")