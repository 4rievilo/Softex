qr = int(input("\nDigite a quantidade de rodas: \n"))
p = float(input("\nDigite o peso bruto em quilogramas: \n"))
qp = int(input("\nDigite o número máximo de pessoas que cabem no veículo: \n"))

if qr <= 1:
    print("\nQuantidade de rodas não permitidas.\n")
elif qr <= 3:
    print("\nCategoria de habilitação: A\n")
elif qr == 4 and qp <= 8 and p <= 3500:
    print("\nCategoria de habilitação: B\n")
elif qr >= 4:
    if p >= 3500 and p <= 6000:
      print("\nCategoria de habilitação: C\n")  
    elif qp > 8:
        print("\nCategoria de habilitação: D\n")
    elif p > 6000:
        print("\nCategoria de habilitação: E\n")
    else:
        print("\nErro.\n")
else:
        print("\nErro.\n")