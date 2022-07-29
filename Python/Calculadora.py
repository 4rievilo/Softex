def calculadora(num1,num2,ope):
    if ope == 1:
        return num1+num2
    elif ope == 2:
        return num1-num2
    elif ope == 3:
        return num1*num2
    elif ope == 4:
        return num1/num2
    else:
        return 0

n1 = float(input("\nDigite o primeiro valor:\n"))
n2 = float(input("Digite o segundo valor:\n"))
o = int(input("Digite '1' para Soma;\nDigite '2' para Subtração;\nDigite '3' para Multiplicação;\nDigite '4' para Divisão;\n"))

cal = calculadora(n1,n2,o)
print(f"{cal:.2f}")