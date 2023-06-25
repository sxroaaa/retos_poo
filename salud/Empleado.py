from Persona import Persona
class Empleado(Persona):
    def __init__ (self, tipoDoc, documento, nombre, apellido, peso, estatura, edad, sexo, cargo, valor_hora, horas_trabajadas, departamento):
        super().__init__(tipoDoc, documento, nombre, apellido, peso, estatura, edad, sexo)
        self.cargo = cargo
        self.valor_hora = valor_hora
        self.horas_trabajadas = horas_trabajadas
        self.departamento = departamento

    def calcularHonorarios(self):
        total = self.valor_hora * self.horas_trabajadas
        reteica = total * 0.00966
        honorarios = total - reteica
        return honorarios
    
    def imprimirEmpleado(self):
        print("Tipo de documento:", self.tipoDoc)
        print("Número de documento:", self.documento)
        print("Nombres:", self.nombre)
        print("Apellidos:", self.apellido)
        print("Cargo:", self.cargo)
        print("Horas trabajadas:", self.horas_trabajadas)
        print("Valor por hora:", self.valor_hora)
        print("Total a pagar:", self.calcularHonorarios())

Empleado = Empleado("CC", "1022924364", "salome", "roa", 62, 1.58, 19, "f", "auxiliar", 4000, 8, "B")
Empleado.imprimirEmpleado()