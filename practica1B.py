# Con Finally
# Creo que esta aproximación no es del todo correcta
# porque si la excepción es lanzada será porque 'fileContent' ha fallado
# por lo tanto en el finally tendremos de nuevo un error al no existir 'fileContent'

# filename = input("Type filename: ")

# try:
#     print('-1- Opening file')
#     fileContent = open(filename, "r")
#     print('-2- File opened')

# except (OSError, IOError) as e:
#     print(e, ' | ', type(e))

# finally:
#     print('-3- Closing file')
#     fileContent.close()
#     print('-4- File closed')

# Con Else
# Creo que esta aproximación sería mejor ya que solo se ejecutará
# si el try ha tenido exito al abrir 'fileContent' y no se ha producido
# ninguna excepción

filename = input("Type filename: ")

try:
    print('-1- Opening file')
    fileContent = open(filename, "r")
    print('-2- File opened')

except (OSError, IOError) as e:
    print(e, ' | ', type(e))

else:
    print('-3- Closing file')
    fileContent.close()
    print('-4- File closed')