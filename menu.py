import random
from Apartamento import Apartamento 
from Lista_encadeada import Lista_vagas
from Fila import Fila


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

def menu_principal():
    lista = Lista_vagas()
    fila = Fila()
    while True:
        print(menu_principal_string)
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            id_ap = random.randint(10,100)
            numero_ap = int(input("Digite o número do apartamento: "))
            lista.add_apartamento(id_ap, numero_ap)
        elif escolha == 2:
            pass
        elif escolha == 3:
            lista.imprimir_vagas()
        elif escolha == 4:
            fila.imprimir_fila()
        elif escolha == 0:
            break

# def digital_choice():
#     apart = random.randit(10,100)
#     return apart