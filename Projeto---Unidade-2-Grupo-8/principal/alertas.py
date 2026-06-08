import os
from datetime import datetime

caminho_atividades = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "dados",
    "atividades.txt"
)

def carregar_atividades():
    atividades = []
    try:
        with open(caminho_atividades, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        item = {}
        for linha in linhas:
            linha = linha.strip()
            if linha.startswith("Pet:"):
                item["pet"] = linha.replace("Pet: ", "", 1)
            elif linha.startswith("Atividade:"):
                item["atividade"] = linha.replace("Atividade: ", "", 1)
            elif linha.startswith("Data:"):
                item["data"] = linha.replace("Data: ", "", 1)
            elif linha.startswith("Responsavel:"):
                item["responsavel"] = linha.replace("Responsavel: ", "", 1)
                atividades.append(item)
                item = {}
    except FileNotFoundError:
        print("Arquivo de atividades não encontrado.")
    return atividades


def dias_restantes(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y").date()
        return (data - datetime.now().date()).days
    except ValueError:
        return None


def exibir_alertas(nome_pet, atividades):
    filtradas = [a for a in atividades if a["pet"].lower() == nome_pet.lower()]

    if not filtradas:
        print(f"\nNenhuma atividade encontrada para '{nome_pet}'.")
        return

    filtradas.sort(key=lambda a: datetime.strptime(a["data"], "%d/%m/%Y"))

    print(f"\n===== ALERTAS — {nome_pet.upper()} =====")
    print(f"Hoje: {datetime.now().strftime('%d/%m/%Y')}\n")

    for a in filtradas:
        dias = dias_restantes(a["data"])

        if dias is None:
            status = "Data inválida"
        elif dias < 0:
            status = f"ATRASADA há {abs(dias)} dia(s)!"
        elif dias == 0:
            status = "HOJE!"
        elif dias <= 7:
            status = f"Faltam {dias} dia(s) — URGENTE"
        else:
            status = f"Faltam {dias} dia(s)"

        print(f"Atividade  : {a['atividade']}")
        print(f"Data       : {a['data']}")
        print(f"Responsável: {a['responsavel']}")
        print(f"Status     : {status}")
        print("-" * 35)


def menu():
    atividades = carregar_atividades()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===== ALERTAS E CONTAGEM REGRESSIVA =====")
        print("1 - Ver alertas de um animal")
        print("2 - Ver todos os alertas")
        print("3 - Sair")

        opcao = input("\nEscolha: ").strip()

        if opcao == "1":
            nome = input("Nome do animal: ").strip()
            if nome:
                exibir_alertas(nome, atividades)
            else:
                print("Nome não pode ser vazio.")
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            if not atividades:
                print("\nNenhuma atividade cadastrada.")
            else:
                todos = sorted(atividades, key=lambda a: datetime.strptime(a["data"], "%d/%m/%Y"))
                print(f"\n===== TODOS OS ALERTAS =====")
                print(f"Hoje: {datetime.now().strftime('%d/%m/%Y')}\n")
                for a in todos:
                    dias = dias_restantes(a["data"])
                    if dias is None:
                        status = "Data inválida"
                    elif dias < 0:
                        status = f"ATRASADA há {abs(dias)} dia(s)!"
                    elif dias == 0:
                        status = "HOJE!"
                    elif dias <= 7:
                        status = f"Faltam {dias} dia(s) — URGENTE"
                    else:
                        status = f"Faltam {dias} dia(s)"
                    print(f"Pet        : {a['pet']}")
                    print(f"Atividade  : {a['atividade']}")
                    print(f"Data       : {a['data']}")
                    print(f"Status     : {status}")
                    print("-" * 35)
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

menu()
