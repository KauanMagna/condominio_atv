from Apartamento import Apartamento
from Fila import Fila

fila = Fila()

class Lista_vagas:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
 
    def add_apartamento(self, cod, numero_ap, torre):
        if self.inicio is None:
            self.inicio = Apartamento(cod, numero_ap, torre)
            ap = self.inicio
            ap.vaga = 1
        elif self.inicio is not None:
            ap = self.inicio
            while ap.proximo:
                ap = ap.proximo
            if ap.vaga <= 9:
                ap.proximo = Apartamento(cod, numero_ap, torre)
                ap.proximo.vaga = ap.vaga + 1
            else:
                apart = Apartamento(cod, numero_ap, torre)
                print("estourou o número de vagas")
                return apart
        self.tamanho += 1
        
    def imprimir_vagas(self):
        ap = self.inicio
        count = 0
        while ap:
            count += 1
            if count >= 11:
                break
            print(f"Número da Vaga: {ap.vaga} \nNúmero do Apartamento: {ap.numero_ap} - ID: {ap.id} - Torre: {ap.torre.nome}")
            ap = ap.proximo
            
    
    def liberar_vaga(self, vaga, fila):
        ap = self.inicio
        anterior = None
        while ap:
            if ap.vaga == vaga:
                print(f"\nApartamento Antigo na vaga: {vaga} \nNúmero: {ap.numero_ap} Vaga e próximo: {ap.vaga}, {ap.proximo}")
                apartamento_novo = fila.remover_fila()
                if apartamento_novo is None:
                    print("A fila está vazia")
                    return None
                apartamento_novo.vaga = ap.vaga
                apartamento_novo.proximo = ap.proximo
                if anterior is None:
                    self.inicio = apartamento_novo
                else:
                    anterior.proximo = apartamento_novo
                print(f"\nApartamento Novo na vaga: {vaga} \nNúmero: {apartamento_novo.numero_ap} Vaga e próximo: {apartamento_novo.vaga}, {apartamento_novo.proximo}")
                return ap
            anterior = ap
            ap = ap.proximo
        print("Vaga não encontrada")
        return None
