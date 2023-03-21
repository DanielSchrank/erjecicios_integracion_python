"""
Este módulo corresponde a los ejercicios integradores subidos al Aula Virtual del Curso de Django

"""
# EJERCICIO 1.
# Escribir una función que calcule el máximo común divisor entre dos números.

def max_com_div(num1, num2):
    """La función toma dos números y guarda en dos listas los números divisibles de cada uno. 
    Luego se transforman en sets para guardar los números que no se repiten y 
    se guarda en una lista la intersección de éstas.
    Finalmente se devuelve el último valor de la lista. """

    div_num1 = []
    div_num2 = []

    for i in range(1, num1+1):
        if num1 % i == 0:
            div_num1.append(i)

    for j in range(1, num2+1):
        if num2 % j == 0:
            div_num2.append(j)

    maxi = list(set(div_num1).intersection(set(div_num2)))
    return maxi[-1]

# EJERCICIO 2.
# Escribir una función que calcule el mínimo común múltiplo entre dos números.


def min_com_mul(num1, num2):
    """La función recibe dos números y los divide por su máximo común divisor y devuelve el resultado"""
    return num1*num2/max_com_div(num1, num2)


# EJERCICIO 3.
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).


def splitear_string(str1):
    """La función recibe un string y devuelve un diccionario con cada palabra y su frecuencia"""
    lista_string = []
    dict_string = {}
    for i in str1.split():
        lista_string.append(i)
    for i in lista_string:
        dict_string.update({i.strip("-/_#,."): lista_string.count(i)})
    return dict_string


# EJERCICIO 4.
# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia


def palabra_mas_frecuente(str1):
    """La función toma un string y devuelve una tupla con la palabra más repetida y su frecuencia"""
    valor_mas_frecuente = sorted(splitear_string(
        str1).items(), key=lambda x: x[1], reverse=True)
    return tuple(valor_mas_frecuente[0])

# EJERCICIO 5.
# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva


def get_int():
    """La función recibe un valor por teclado y devuelve el valor solo si es un entero."""
    return  # To be done.

# EJERCICIO 6
# Crear una clase llamada Persona.  Sus atributos son: nombre, edad y DNI.
# Construya los siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# - mostrar(): Muestra los datos de la persona.
# - Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.


class Persona:
    """ Clase persona. Atributos: nombre, edad, DNI"""

    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        """ Getter para el atributo nombre"""
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        """ Setter para el atributo nombre"""
        self.__nombre = nombre

    @property
    def edad(self):
        """ Getter para el atributo edad"""
        return self.__edad

    @edad.setter
    def edad(self, edad):
        """ Setter para el atributo edad"""
        self.__edad = edad

    @property
    def dni(self):
        """ Getter para el atributo DNI"""
        return self.__dni

    @dni.setter
    def dni(self, dni):
        """ Setter para el atributo DNI"""
        self.__dni = dni

    def mostrar(self):
        """ Muestra los datos completos de la persona"""
        print(f"{self.__nombre} de {self.__edad} años de edad y DNI nº {self.__dni}")

    def es_mayor_de_edad(self):
        """ Devuelve true si la edad de la persona es mayor o igual a 18"""
        return self.__edad >= 18


# EJERCICIO 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
# - mostrar(): Muestra los datos de la cuenta.
# - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
# - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.

class Cuenta:
    """ Clase cuenta - Atributos titular (persona) y cantidad (flotante)"""

    def __init__(self, titular=Persona(), cantidad=0.0):
        if not isinstance(titular, Persona):
            raise ValueError("El titular debe ser un objeto persona")
        if titular.nombre == "":
            raise ValueError("El titular debe tener nombre")
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        """ Getter para el atributo titular"""
        return self.__titular

    @titular.setter
    def titular(self, titular):
        """ Setter para el atributo titular"""
        self.__titular = titular

    @property
    def cantidad(self):
        """ Getter para el atributo cantidad"""
        return self.__cantidad

    def ingresar(self, cantidad):
        """ Permite el ingreso de una cantidad que se agrega al saldo
        de la cuenta. Si se ingresan cantidades negativas no tienen efecto"""
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("La cantidad ingresada no puede ser negativa. Vuelva a intentarlo.")

    def retirar(self, cantidad):
        """ Permite el retirar una cantidad que se resta del saldo"""
        if cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
        else:
            print(
                "La cantidad requerida no puede ser mayor al saldo actual en la cuenta.")

    def mostrar(self):
        """ Muestra los datos de la cuenta"""
        print(f"El titular es {self.__titular.mostrar()}")
        print(f"Su saldo actual es de {self.__cantidad} ARS")

# EJERCICIO 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuentaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
# - Un constructor.
# - Los setters y getters para el nuevo atributo.
# - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
# - Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.


class CuentaJoven(Cuenta):
    """ Clase CuentaJoven que hereda atributos de la clase Cuenta 
    y se le agrega el atributo de Bonificación """

    def __init__(self, titular=Persona(), cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        """ Getter del atributo bonificación"""
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        """ Setter para el atributo bonificación """
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        """El titular tiene que ser mayor de 18 y menor de 25 años"""
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25

    def retirar(self, cantidad):
        """ Permite el egreso de una cantidad en pesos de se resta del saldo
        Solo puede retirar si el titular es válido"""
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        """ Muestra los datos completos de la persona"""
        print("***   Cuenta Joven   ***")
        super().mostrar()
        print(f"El titular tiene una bonificación del {self.__bonificacion}%")
