# Personagem: clase mãe
# Herói: controlado pelo usuário
# Inimigo: adversário do usuário

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\ntipo: {self.get_tipo()}\n"

class Jogo: 
    """Class orquestradora do jogo"""

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Carlos", vida=40, nivel=5, habilidade="Rodar")
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="voador")
    
    def iniciar_batalha(self):
        """"Fazer a gestão da batalha em turnos"""
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enteder para atecar...")
            escolha = input ("Escolha (1- Ataque Normal, 2 - Ataque Especial):")

# Cria instancia do jogo e inicar batalha
jogo = Jogo()
jogo.iniciar_batalha()