nome = input("\nDigite nome do aluno: \n")
nota1 = float(input("\nDigite a primeira nota: \n"))
nota2 = float(input("\nDigite a segunda nota: \n"))
faltas = int(input("\nDigite a quantidade de faltas: \n"))
media = (nota1/nota2)/2

if media >= 7 or faltas < 3:
    print(f"\nO aluno {nome} está aprovado. \n")
else:
    print(f"\nO aluno {nome} está reprovado. \n")