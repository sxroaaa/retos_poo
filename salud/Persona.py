class Persona:
    tipoDoc=''
    documento=''
    nombre=''
    apellido=''
    peso=''
    estatura=''
    edad=''
    sexo=''

    def __init__(self, tipoDoc, documento, nombre, apellido, peso, estatura, edad, sexo):
       self.tipoDoc=tipoDoc
       self.documento=documento
       self.nombre=nombre
       self.apellido=apellido
       self.peso=peso
       self.estatura=estatura
       self.edad=edad
       self.sexo=sexo
    
    def pediDatos(self):
        self.tipoDoc=input("Digite su tipo de documento:")
        self.documento=input("digite su numero de documento:")
        self.nombre=input("digite su nombre, porfavor:):")
        self.apellido=input("digite su apellido:")
        self.peso=float(input("digite su peso:"))
        self.estatura=float(input("digite su estatura:"))
        self.edad=int(input("digite su edad:"))
        self.sexo=input("digite su sexo:")

    def mostrarDatos(self):
       print(f"hola {self.nombre} {self.apellido} con tipo de documento {self.tipoDoc} y numero {self.documento} tienes un peso de {self.peso} cm, una estatura de {self.estatura} tienes {self.edad} años y tu sexo es  {self.sexo}") 

    def calcularlmc(self):
        pesoActual=round(self.peso/ pow(self.estatura,2),1)
        if pesoActual<20:
            print("el peso esta por debajo de lo ideal")
        if pesoActual<25:
            print("el peso es ideal")
        if pesoActual>25:
            print("tiene sobrepeso")
        print("Su IMC es de "+str(pesoActual))
     
        
        
    def mayorEdad(self):
        if self.edad<18:
            print(f"Hola {self.nombre} aun eres menor de edad:)")
        if self.edad>=18:
            print(f"Hola {self.nombre} ya eres mayor de edad:)")
        

