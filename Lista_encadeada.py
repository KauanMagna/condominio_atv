from Apartamento import Apartamento

class Lista_vagas:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        
    def add_apartamento(self, cod, numero_ap):
        if self.inicio is None:
            self.inicio = Apartamento(cod, numero_ap)
            self.tamanho += 1
            ap = self.inicio
            ap.vaga = 1
        elif self.inicio is not None:
            ap = self.inicio 
            while ap.proximo:
                ap = ap.proximo
            ap.proximo = Apartamento(cod, numero_ap)
            ap.proximo.vaga = ap.vaga + 1
             
    def imprimir_vagas(self):
        ap = self.inicio
        count = 0
        while ap:
            count += 1
            if count >= 6:
                break
            print(f"Número do Apartamento: {ap.numero_ap} \nNúmero da Vaga: {ap.vaga}")
            ap = ap.proximo
        
           
    def liberar_vaga(self, vaga):
        ap = self.inicio
        while ap:
            if ap.vaga == vaga:
                print(f"Apart: {ap.numero_ap} \nVaga: {ap.vaga}")
                break
            ap = ap.proximo
        print("Fim")

            
