
class Apartamento:
    def __init__(self, cod, numero_ap, torre):
        self.id = cod 
        self.numero_ap = numero_ap
        self.torre = torre
        self.vaga = None
        self.proximo = None
    
    #Cadastrar apartamento em lista_encadeada
    
    def __str__(self):
        return (f"Apartamento ID: {self.id}, Número: {self.numero_ap}, Torre: {self.torre}, Vaga: {self.vaga}, Próximo: {self.proximo.numero_ap}")
    