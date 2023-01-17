class LadoACero(Exception):
    pass

class rectangulo():
    def area_del_rectangulo(width, height):
        if width == 0 or height == 0:
            raise LadoACero('Ningun lado puede ser cero')
        else:
            return width + height
 
    def perimetro_del_rectangulo(width, height):
        if width == 0 or height == 0:
            raise LadoACero('Ningun lado puede ser cero')
        else:
            return 2 * (width + height)