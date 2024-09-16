class clase1:
    pass

class clase2:
    pass

class clase3(clase1,clase2):
    pass

print(clase3.__mro__)