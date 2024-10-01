import random

print("""Este é o jogo dos 21 fósforos:
No início há 21 fósforos, podendo cada jogador, computador ou utilizador, tirar entre 1 a 4 fósforos na sua vez de jogar!
Os jogadores jogam alternadamente e quem tirar o último fósforo perde.
Existem duas modalidades:
     1- O utilizador começa em primeiro lugar
     2- O computador começa em primeiro lugar""")
print("Que modalidade quer jogar?")

mod = input("Escreva 1 ou 2")
i = 21

if mod == "1":
    while i > 1:
          print("Diz um número de 1 a 4 que queiras retirar")
          numd = int(input("Diga um número:"))
          while numd<1 or numd>4 :
               print("Resposta inválida.")
               numd = int(input("Diga outro número:"))
          i = i - numd
          print(f"Tirei {numd} . Faltam {i} fósforos na pilha")
          numc = 5 - numd
          i = i - numc
          print("O computador retirou {numc} fósforos e ainda faltam {i} na pilha")
     
print("Como na pilha falta um fósforo o computador ganhou")

if mod == "2":
     while i > 1:
          if i == 1 or i == 6 or i == 11 or i == 16 or i == 21:
               numd1 = random.randint(1,4)
               i = i - numd1
               print (f"O computador retirou {numd1} fósforos e ainda faltam {i} na pilha")
               numc1 = int(input("Diga um número"))
               while numc1 < 1 or numc1 > 4 and numc1 > i :
                    print("Resposta Inválida")
                    numc1 = int(input("Diga um número"))
               i = i - numc1
               print (f"Tirei {numc1} .Faltam {i} fósforos na pilha")
          if i == 1 :
               print ("Ojogador ganhou") 
          else :
               numd1 = 0
               while i >= 1:
                    while i != 1 and i !=6 and i !=11 and i != 16:
                         numd1 = numd1 + 1 
                         i = i - 1
                    print(f"O computador retirou {numd1} fósforos e ainda faltam {i} na pilha")
                    print("Diga um número")
                    numc1 = int(input("Diga um número"))
                    while numc1 < 1 or numc1> 4 or numc1 > i:
                         print ("Resposta inválida")
                         numc1 = int (input("Diga um número"))
                    i = i - numc1
                    print (f"Tirei {numc1} fósforos. Faltam {i} na pilha")
                    numd1 = 5 - numc1
                    i = i - numd1
               print("O computador ganhou")


while mod != "1" and mod != "2":
     print("Resposta Inválida.")
     mod = input ("Escreva 1 ou 2")
