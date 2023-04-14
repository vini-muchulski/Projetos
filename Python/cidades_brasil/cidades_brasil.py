class Cidade:
    def __init__(self,nome,pop,estado):
        self.nome = nome
        self.pop = pop
        self.estado = estado

    
    def get_cidade(self):
        print(f"A cidade de {self.nome} no estado de {self.estado} tem uma populacao de {self.pop}")

    def atualiza_pop(self, populacao_nova):
        self.pop = populacao_nova
        
        
        