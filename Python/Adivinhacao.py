print("Jogo da Adivinhação!\n")
print("Tente acertar o valor de 1 a 10. Você tem 3 chances.")

numero_secreto = 4
c = True
while c is True:
  try:
    for i in range(3):
      print(f"\nChance número {i+1}:")
      chute = int(input("Qual o número?  "))
      if chute == numero_secreto:
        print("\nParabéns, você acertou!")
        c = False
        break
      elif chute > numero_secreto:
        print("\nO número é menor!")
      elif chute < numero_secreto:
        print("\nO número é maior!")
  except:
    print("\nPor favor, digite apenas números")
  if i == 2:
    c = False

if (i == 2) and chute != numero_secreto:
  print("\nVocê perdeu!")