def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)

def par_impar(numero):
    multiplo_De_dois = numero % 2 == 0
    
    if multiplo_De_dois:
        return f"{numero} é par"
    
        
    return f"{numero} é impar"
    
print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))