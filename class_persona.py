class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    
    def __add__(self,other):     #obj1.__add__(obj2)  obj2 seria other
        return f"{self._nombre} {other._nombre}"
 
    def __sub__(self,otro):
        return self._edad - otro._edad

persona1 = Persona("JUAN",45)
persona2 = Persona("CARLOS",15)
print(persona1 + persona2) #al imprimir concatena los nombres
print(persona1 - persona2) #al imprimir resta las edades