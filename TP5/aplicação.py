def menu():
    print(""" -------------Menu---------------
          1- Listar as salas e os filmes respetivos
          2- Verificar se um lugar está disponível
          3- Vender o bilhete para um lugar disponível
          4- Listar a sala, o filme e o número de lugares disponíveis.
          5- Inserir uma nova sala ao cinema
          6- Remover uma sala
          7- Dar reset ao cinema
          8- Sair do menu
            """)
    
def existeSala(cinema, nome):
    cond=False
    for sala in cinema:
        if sala[3]== nome:
            cond =True 

    return cond

def listar(cinema):
    print("------------Lista de Filmes-------------")
    for s in cinema:
        nlugares, vendidos, filme, nome =s
        print(f"Sala:{nome}| Nome do filme:{filme}")
    print("------------------------------------------")
    return

def disponivel( cinema, filmes, lugar ):
    cond=False
    for s in cinema:
        nlugares, vendidos, filme, nome =s
        if filme==filmes and lugar <= nlugares:
            if lugar not in vendidos:
                cond= True
    return cond

def vendebilhete( cinema, filmes, lugar):
    if disponivel( cinema, filmes, lugar ):
        for s in cinema:
            nlugares, vendidos, filme, nome = s
            if filme == filmes:
                vendidos.append(lugar)
    return cinema

def listardisponibilidades(cinema):
    for s in cinema:
        nlugares, vendidos, filme, nome =s
        print(f"Sala: {nome}| Filme:{filme} |Nº de disponiveis:{nlugares-len(vendidos)}")
    return 

def inserirSala(cinema, nome, filme, lugares):
    vendidos=[]
    s= (lugares, vendidos, filme, nome)
    
    if not existeSala(cinema, nome):
        cinema.append(s)       
    return cinema

def removeSala(cinema, filme):
    for s in cinema:
        nlugares, vendidos, filme, nome=s
        if vendidos==[]:
            cinema.remove(s)
    return cinema

cond2=True
cinema=[]
while cond2:
    menu()
    opcao = input("Introduza uma opção")

    while opcao not in ["1","2","3","4","5","6","7","8","9","0"]:
        print("Resposta inválida!! Tente novamente.")
        opcao=input("Introduza uma opção")

    if opcao== "1":
        listar(cinema)

    elif opcao=="2":
        filmes = input("Diga o filme que quer:")
        lugar= int(input("Diga o lugar que quer verificar se está disponível:"))        
        disponivel( cinema, filmes, lugar )
    
    elif opcao=="3":
        filmes = input("Diga o filme que quer:")
        lugar= int(input("Diga o lugar que quer verificar se está disponível:"))       
        vendebilhete( cinema, filmes, lugar)
    
    elif opcao=="4":
        listardisponibilidades(cinema)

    elif opcao=="5":
        nome= input("Diga i número da sala que quer ver se existe")
        filme = input("Diga o filme que quer:")
        lugares= int(input("Diga o lugar que quer verificar se está disponível:"))
        inserirSala(cinema, nome, filme, lugares)

    elif opcao=="6":
        filme = input("Diga o filme que quer:")
        removeSala(cinema, filme)
    
    elif opcao=="7":
        cinema.clear()
        print("O cinema sofreu um reset")
            
    elif opcao == "8":
        cond2 = False
print("Até à próxima!")
