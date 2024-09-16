class Clase:
    atributo_clase = "Hola"  # Es accesible desde el exterior
    __atributo_clase = "hola no se ve"  # No accesible desde el exterior
    
    def __mi_metodo(self):  # Método privado
        print("Haz algo")
        self._variable = 0  # Atributo protegido
    
    def metodo_normal(self):  # Método accesible desde el exterior
        # Llamada al método privado dentro de la clase
        self.__mi_metodo()


# Crear una instancia de la clase
mi_clase = Clase()

# Acceder al atributo público
print(mi_clase.atributo_clase)  # Salida: Hola

# Intentar acceder al atributo privado desde el exterior da error
# print(mi_clase.__atributo_clase)  # Esto genera un AttributeError

# Llamar al método accesible
mi_clase.metodo_normal()  # Salida: Haz algo
