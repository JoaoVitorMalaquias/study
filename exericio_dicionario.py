perguntas = [
    {
    "Pergunta" : "Quanto é 20+20",
    "Opcoes" : ["18", "30", "40", "2000"],
    "Resposta" : "40" ,         
    },
    {
    "Pergunta" : "Quanto é 2*2",
    "Opcoes" : ["1", "3", "4", "20"],
    "Resposta" : "4",
    },
    {
    "Pergunta" : "Quanto é 10/2",
    "Opcoes" : ["1", "3", "4", "5"],
    "Resposta" : "5",
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print("Pergunta: ", pergunta["Pergunta"])
    print()
    
    opcoes = pergunta["Opcoes"]
    for i , opcao in enumerate (opcoes):
        print(f"{i})",opcao)
    print()
    
    escolha = input("Escolha uma opcao: ")
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta["Resposta"]:
                acertou = True
    print()
    if acertou:
        qtd_acertos += 1
        print("Resposta Certa")
    else:
        print("Resposta Errada")
        
    print()
    
print("Voce acertou", qtd_acertos)
print("de", len(perguntas), "perguntas.")