import os

lista = []
while True:
    print("Selecione uma opcao")
    opcao = input("[i]nserir [a]pagar [l]istar: ")
    
    if opcao == "i":
        os.system("clear") #limpar o terminal
        valor = input("Valor: ") # exibir o valor
        lista.append(valor)
    elif opcao == "a":
        indice_str = input(
            "Escolha o indice para pagar: "
        )
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print("Por favor digite um numero inteiro.")
        except IndexError:
            print("Indice nao existe na lista")
        except Exception:
            print("Erro desconhecido")
    elif opcao == "l":
        os.system("clear")
        
        if len(lista) == 0:
            print("Nada para listar")
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print("Por favor escolha uma opcao correta" )
