
    

lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]


for x in zip(lista_a,lista_b):
    lista_a += lista_b
    print(list(x))
    print(sum(list(x)))

# ou
print()

lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma =[x + y for x,y in zip(lista_a,lista_b)]
print(lista_soma)


#ou
print()

lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma1= []
for i in range(len(lista_b)):
    lista_soma1.append(lista_a[i] + lista_b[i])

print(lista_soma1)