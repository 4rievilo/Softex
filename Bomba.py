import time

s = int(input("\nDigite quantos segundos até a bomba explodir:\n"))
print("\nINICIANDO CONTAGEM REGRESSIVA\n")
for i in range(s, 0, -1):  
    print(f"{i}")
    time.sleep(1)
print("\nBUMMM!!\n")