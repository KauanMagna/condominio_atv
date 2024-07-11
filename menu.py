import random
from Lista_encadeada import Lista_vagas, fila
from Torre import Torre


menu_principal_string = """
===============
Menu Principal
===============
0 - Sair
1 - Cadastrar Apartamento
2 - Liberar Vaga
3 - Imprimir Apartamentos nas Vagas
4 - Imprimir lista de Espera por Vagas
"""
torre01 = Torre(12, "Magnus", "Rua Antonieta")

def menu_principal():
    lista = Lista_vagas()
    while True:
        print(menu_principal_string)
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            id_ap = random.randint(10,100)
            numero_ap = int(input("Digite o número do apartamento: "))
            torre = torre01
            ap_espera = lista.add_apartamento(id_ap, numero_ap, torre)
            fila.adicionar(ap_espera)
        elif escolha == 2:
            ap_espera = lista.liberar_vaga(int(input("Escolha uma vaga entre 1 e 10: ")), fila)
            fila.adicionar(ap_espera)
        elif escolha == 3:
            lista.imprimir_vagas()
        elif escolha == 4:
            fila.imprimir_fila()
        elif escolha == 0:
            break
