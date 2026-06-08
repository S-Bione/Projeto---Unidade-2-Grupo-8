from crud import acao, repeticao
from atividades import acao_atividade
from alertas import exibir_alertas
from sugestao import mostrar_sugestoes
import os

def inicio():
    try:
    print("------TELA INICIAL-------\n")

    acao_inicial = int(input("1 - Itens relacionados a cadastro do pet\n2 - Itens relacionados a atividades do pet\n3 - Alertas do pet\n4 - Sugestões pet\nEscolha: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if (acao_inicial == 1):
        acao()
        repeticao()
    elif acao_inicial == 2:
        acao_atividade()
    elif acao_inicial == 3:
        exibir_alertas()
    elif acao_inicial == 4:
        mostrar_sugestoes()
    else:
        print("Opção inválida, insira um valor válido.")
        inicio()
    except ValueError:
        
inicio()