class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando"

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcego emitem sons ultrassonicos"

morcego = Morcego(nome="Batman")

#acessando métodos da classe base Animal
print("Nome do Morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

#Acessano métodos das classes mamifero e ave
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())