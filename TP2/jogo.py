import random

print ("Este é o jogo adivinha o número. Tem duas modalidades: \n 1- O pc pensa num número e o jogador tenta adivinhar; \n 2- O jogador pensa num número e o pc adivinha")
print ("Quem pensa no número terá de então responder se a tentativa foi correta, maior ou menor")
print("Qual modalidade quer jogar? 1 ou 2?")
mod = input ("qual modalidade quer jogar?1 ou 2?")

while mod != "1" and mod != "2":
    print("resposta inválida. Modalidade 1 ou 2?")
    mod = input("Qual modalidade quer jogar? 1 ou 2?")

if mod == "1":
    print ("Diga um número")
    numcomp = random.randint(0,100)
    ten = int(input("Diga um número"))
    tent = 1
    if ten == numcomp:
        print("Acertou!!")
    while ten != numcomp:
        tent = tent + 1
        if ten > numcomp:
            print ("O número que pensei é mais baixo. Tente outra vez.")
            ten = int(input("Diga um número"))
        elif ten < numcomp:
            print ("O número que pensei é mais baixo. Tente outra vez")
            ten = int(input("Diga um número"))
    print(f"Acertou em {tent} tentativas!!")

if mod == "2":
    print("Vou tentar adivinhar o seu número")
    print("O seu número é 50?")
    res = input("Se sim escreva acertou, se for maior escreva maior e se for menor escreva menor")

    while res!="acertou" and res!= "menor" and res!= "maior":
        print ("Resposta inválida. Escreva acertou, maior ou menor.")
        print ("O seu número é 50?")
    res = input ("Se sim escreva acertou, se for maior escreva maior e se for menor escreva menor")
    print(res)

tent2 = 1 
min = 0
max = 100
ini = 50

if res == "Acertou":
    print(f"Acertei à primeira tentativa!!")
while res == "menor"or res == "maior":
    tent2 = tent2 + 1 
    if res == "menor":
        max = ini + 1
        ini = (max + min)// 2
    elif res == "maior":
        min = ini + 1
        ini = (max + min)// 2
    print(f"O seu número é {ini}? Se sim escreva acertou, se for Maior escreva maior e se for Menor escreva menor")
    res = input (f"O seu número é {ini}? Se sim escreva acertou, se for Maior escreva maior e se for Menor escreva menor")
    while res != "acertou" and res != "menor" and res != "maior":
        print("Resposta inválida. Escreva acertou, maior ou menor.")
        print(f"O seu número é {ini}?")
        res = input ("Se sim escreva acertou, se for Maior escreva maior e se for Menor escreva menor")
print (f"Acertei após {tent2} tentativas!!")
    





