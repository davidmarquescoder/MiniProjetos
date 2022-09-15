class Secretas():
    def __init__(self, nome, dicas, ajudar = False):
        self.nome = nome
        self.dicas = dicas
        self.ajudar = ajudar
    
    def dar_dica(self):
        print(self.dicas)
        self.ajudar = True