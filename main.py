from Torre import Torre
from Apartamento import Apartamento 
from Lista_encadeada import Lista_vagas

"""
01- Criar classes Torre e Apartamento
02- Criar uma lista encadeada para as vagas
03- Criar uma fila para a espera
        a- método para adicionar ap na fila
        b- método para tirar o ap da fila
        c- método para imprimir a fia
"""
lista = Lista_vagas()
lista.add_apartamento(1010, 10)

lista.add_apartamento(1010, 20)
lista.add_apartamento(1010, 15)
lista.add_apartamento(1010, 2)

lista.imprimir_vagas()
lista.liberar_vaga(int(input("Vaga: ")))
#lista.imprimir_vagas()