class Miexcepcion(Exception):
    'Raise cuando el input es mayor que 10'
    pass

top = 10

try:
    valor = int(input('Introduce un valor: '))
    if valor > top:
        raise Miexcepcion
    
except Miexcepcion as e:
    print('El número es mayor que 10. Introduce un número menor.')

except ValueError:
    print('No es un valor válido. Por favor, introduce un número.')