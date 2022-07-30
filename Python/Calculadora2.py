def calculadora(num1,num2,ope):
    if ope == 1:
        return num1+num2
    elif ope == 2:
        return num1-num2
    elif ope == 3:
        return num1*num2
    elif ope == 4:
        return num1/num2
    elif ope == 0:
        return 0

o = 3
while o != 0:
    n1 = float(input("\nDigite o primeiro valor:\n"))
    n2 = float(input("Digite o segundo valor:\n"))
    o = int(input("Digite '1' para Soma;\nDigite '2' para Subtração;\nDigite '3' para Multiplicação;\nDigite '4' para Divisão;\nDigite '0' para Sair;\n"))
    if o <= 4 and o >= 0:
        cal = calculadora(n1,n2,o)
        print(f"{cal:.2f}")
    else:
        print("Essa opção não existe")