class Persona: #Las clases la primera siempre en mayúscula
    def __init__(self, nombre, año, ciudad, apellido, color, animal):
        self.nombre = nombre #atributos
        self.año = año
        self.edad = 2024-año
        self.ciudad = ciudad #atributos inventados
        self.apellido = apellido
        self.color = color
        self.animal = animal

    def saludar(self): #Métodos
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.") # f es Format para meter todo tipo de variables para poder hacer lo de {}
    def queja(self): #Modalidades inventadas
        print(f"Vivo en {self.ciudad} y estoy cansado de ello.") 
    def familia(self):
        print(f"Mi apellido es {self.apellido}.")
    def favoritos(self):
        print(f"Mi color favorito es el {self.color} y mi animal favorito el {self.animal}.")

nombrepropio = input("Por favor, introduce tu nombre: ")
añopropio = int(input("Por favor, introduce tu año de nacimiento: "))
ciudadpropia = input("Introduzca su ciudad: ") #Atributos inventados
apellidopropio = input("Introduzca su apellido: ")
colorpropio = input("Introduzca su color favorito: ")
animalpropio = input("Introduzca su animal favorito: ")


infop = Persona(nombrepropio, añopropio, ciudadpropia, apellidopropio, colorpropio, animalpropio)
infop.saludar()
infop.queja()
infop.familia()
infop.favoritos()