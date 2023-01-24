
#O ZIP ELE É USADO PARA PEGAR A LISTA MENOR

from itertools import zip_longest
#ESSE ZIP LONGEST ELE PEGA A LISTA MAIOR
from dados_unir_lista import lista1, lista2

def zipper(lista1,lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]
    

l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]

print(zipper(l1,l2))

print()
#JEITO MAIS FACIL

l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]

print(list(zip(l1,l2)))

#ou 
print()

for x in zip(l1,l2):
    print(list(x))
    
    
print()
 #pega a lista maior
for x in zip_longest(l1,l2, fillvalue="SEM CIDADE"):
    print(list(x))
    