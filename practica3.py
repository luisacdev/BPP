"""
# Codigo Python para gestionar una Wallet
"""

class InsuficienteSaldo(Exception):
    "## Excepcion creada para gestionar la posibilidad de no tener saldo suficiente"
    pass


class wallet():
    "## Creacion de la clase Wallet"
    def __init__(self, cantidad = 0):
        "### Asignamos saldo a cero al crear la Wallet"
        self.saldo = cantidad
    

    def gastar_dinero(self, cantidad):
        """
        ### Creamos una funcion para gastar dinero:   
        En caso que el saldo sea inferior a la cantidad a gastar ejecutamos la excepcion   
        De lo contrario, si hay suficiente, se realiza el descuento de la cantidad
        """
        if self.saldo < cantidad:
            raise InsuficienteSaldo('No hay saldo suficiente en tu cuenta')
        else:
            self.saldo -= cantidad
           
    
    def ingresar_dinero(self, cantidad):
        """
        ### Creamos una funcion para ingresar dinero a la wallet:   
        Sumando el saldo con la cantidad deseada
        """
        self.saldo += cantidad
        