# Ejercicio 1

#import pdb
#pdb.set_trace()

listas = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
resultado1 = [max(i) for i in listas]

## Conclusion
"""
No soy capaz de obtener ninguna conclusion con pbd
quizas es por que he utilizado una funcion nativa de Python max()
"""

# Ejercicio 2
lista = [3, 4, 8, 5, 5, 22, 13]
def esPrimo(lista):
    for numero in lista:  
        if numero > 1:  
            for j in range(2, int(numero/2) + 1):  
                if (numero % j) == 0:    
                    break  
            else:  
                return numero  
        else:  
            break
        
resultado2 = filter(esPrimo, lista)