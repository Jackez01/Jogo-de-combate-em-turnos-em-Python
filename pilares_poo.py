#Herança
from typing import Any


print("\nExemplo de herança:")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def andar(self):
        print("O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"