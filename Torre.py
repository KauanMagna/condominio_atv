class Torre:
    def __init__(self, cod, nome, endereco):
        self.id = cod 
        self. nome = nome
        self.endereco = endereco
        
        
        def __str__(self):
            return (f"Torre ID: {self.id}, Nome: {self.nome}, Endereço: {self.endereco}, Quantidade de Apartamentos: {len(self.apartamentos)}")