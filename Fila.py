from Apartamento import Apartamento

class Fila:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0

    def adicionar(self, objeto):
        apartamento = objeto
        if self.final is None:
            self.inicio = apartamento
            self.final = apartamento
        elif self.final is not None:
            self.final.proximo = apartamento
            self.final = apartamento 
        self.tamanho += 1  
    
    def imprimir_fila(self):
        ap = self.inicio
        if self.tamanho == 0:
            print("A Fila está vazia!")
        else:
            while ap:
                print(f"Número do apartamento: {ap.numero_ap}")
                ap = ap.proximo
            
    #def remover_fila(self):
        