def vencedor(a,b,c):
    if (a >= b and a >= c):
        if (a > b and a > c):
            return "candidato_X venceu"
        elif (a == b and a > c):
            return "impate entre candidato_X e candidato_Y"
        elif (a == c and a > b):
            return "impate entre candidato_X e candidato_Z"
    if (b >= a and b >= c):
        if (b > a and b > c):
            return "candidato_Y venceu"
        elif (b == a and b > c):
            return "impate entre candidato_X e candidato_Y"
        elif (b == c and b > a):
            return "impate entre candidato_Y e candidato_Z"
    if (c >= a and c >= b):
        if (c > a and c > b):
            return "candidato_Z venceu"
        elif (c == a and c > b):
            return "impate entre candidato_X e candidato_Z"
        elif (c == b and c > a):
            return "impate entre candidato_Y e candidato_Z"

x = 0 
y = 0 
z = 0 
b = 0 
n = 0
v = 1
k = 2
ven, cx, cy, cz, cb, cn = "", 0,0,0,0,0

while (v == 1):
    while True:
        try:
            print("\nDigite o número do seu candidato:\n")
            voto=int(input("- candidato_X => 889\n- candidato_Y => 847\n- candidato_Z => 515 \n- branco => 0 \n\n"))
            if (voto == 889):
                x=x+1
                print("Voto computado no candidato X.\n")
                break
            elif (voto == 847):
                y=y+1
                print("Voto computado no candidato Y.\n")
                break
            elif (voto == 515):
                z=z+1
                print("Voto computado no candidato Z.\n")
                break
            elif (voto == 0):
                b=b+1
                n=n+1
                print("Voto computado como branco.\n")
                break
            else:
                n=n+1
                print("Voto computado como nulo.\n")
                break
        except Exception as erro:
            print("\nPor favor, digite apenas números.")
    while True:
        try:
            k=int(input("Deseja continuar a votação?\n1. Sim\n2. Não\n"))
            if k==1 or k==2:
                break
        except Exception as erro:
            print("Por favor, digite apenas números.\n")
    v=k

ven = vencedor(x,y,z)
print(f"Resultado da eleição:{ven}!\n{x} votos para o candidato_X;\n{y} votos para o candidato_Y;\n{z} votos para o candidato_Z;\n{b} votos brancos;\n{n} votos nulos.")
    





