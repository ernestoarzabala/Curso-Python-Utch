# Archivo ejemplo 00 de creacion de clases en Python

from math import gcd # greatest common denominator = Maximo Comun Divisor (MCD)

class Fraccion:
    """ La clase Fraccion: Una fraccion es un part de enteros: un numerador (num)
        y un denominador (den !=0 ) cuyo MCD es 1.
    """

    def __init__(self,numerador,denominador):
        """ Constructor de la clase. Construye una fracción a partir de dos enteros:
            un numerador y un denominador.
            ¡El constructor se enloquece si el denominador es cero! 
            Nota mental:Agregar manejo de error para denominador igual a cero.
        """
        hcf = gcd(numerador,denominador)
        self.num, self.den = numerador/hcf, denominador/hcf

    def __str__(self):
        """ Generador de strings para representar una fracción.
            Se necesita si se desea convertir ,o mostrar, una fraccion a string.
        """
        return "%d/%d" % (self.num,self.den)

    def __mul__(self,otrafraccion):
        """ Función necesaria para el operador de multiplicación.
            Multiplica dos fracciones para obtener una fraccion resultante
        """
        return Fraccion(self.num*otrafraccion.num,self.den*otrafraccion.den)

    def __add__(self,otrafraccion):
        """Función necesaria para el operador de suma.
            Suma dos fracciones para obtener una fraccion resultante
        """
        return Fraccion(self.num*otrafraccion.den+self.den*otrafraccion.num,self.den*otrafraccion.den)

    def a_numero_real(self):
        """ Función para convertir la fracción a un numero de punto flotante.
            El equivalente numérico con punto decimal de la fracción.
        """
        return float(self.num)/float(self.den)


if __name__ == "__main__":
    a = Fraccion(3,7)
    b = Fraccion(25,56)
    c = a*b
    c_real = c.a_numero_real()
    print("Multiplicar la fraccion {} por la fraccion da como resultado la fraccion {} que es equivalente a {}".format(a,b,c,c_real))