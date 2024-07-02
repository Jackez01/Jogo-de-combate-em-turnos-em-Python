#Herança



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
    
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de polimorfismo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de emcapsulamento")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_zezinho = ContaBancaria(saldo=50)

print("\nExemplo de abstração")
from abc import ABC, abstractclassmethod

class Veiculo(ABC):

    @abstractclassmethod
    def ligar(self):
        pass

    @abstractclassmethod    
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
       pass

    def ligar(self):
        return "Carro ligando usando a chave"
    
    def desligar(self):
        return "Carro desligou usando a chave"

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())