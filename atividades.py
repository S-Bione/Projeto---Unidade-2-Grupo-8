from datetime import datetime

atividades = []

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def salvar_em_txt():
    with open("atividades.txt", "w", encoding="utf-8") as f:
        f.write("=== ATIVIDADES ===\n\n")
        for item in atividades:
            f.write(f"Pet: {item['pet']}\n")
            f.write(f"Atividade: {item['atividade']}\n")
            f.write(f"Data: {item['data']}\n")
            f.write(f"Responsavel: {item['responsavel']}\n")
            f.write("\n")

def carregar_txt():
    try:
        with open("atividades.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        
        item = {}
        for linha in linhas:
            linha = linha.strip()
            if linha.startswith("Pet:"):
                item["pet"] = linha.replace("Pet: ", "")
            elif linha.startswith("Atividade:"):
                item["atividade"] = linha.replace("Atividade: ", "")
            elif linha.startswith("Data:"):
                item["data"] = linha.replace("Data: ", "")
            elif linha.startswith("Responsavel:"):
                item["responsavel"] = linha.replace("Responsavel: ", "")
                atividades.append(item)
                item = {}
    except FileNotFoundError:
        pass

def cadastrar_atividade():
    print("\n--- Cadastro de Atividade ---")
    nome_pet = input("Nome do animal: ")
    atividade = input("Atividade: ")
    data = input("Data (dd/mm/aaaa): ")
    responsavel = input("Responsável: ")

    if nome_pet == "" or atividade == "" or data == "" or responsavel == "":
        print("Erro: Todos os campos devem ser preenchidos!")
        return

    if not validar_data(data):
        print("Erro: Data inválida! Use o formato dd/mm/aaaa.")
        return

    dados_atividades = {
        "pet": nome_pet,
        "atividade": atividade,
        "data": data,
        "responsavel": responsavel
    }
    atividades.append(dados_atividades)
    salvar_em_txt()
    print("Atividade cadastrada com sucesso!")

def listar_atividades():
    print("\n--- Lista de Atividades ---")
    if len(atividades) == 0:
        print("Nenhuma atividade cadastrada.")
    else:
        for item in atividades:
            print("-" * 30)
            print("Pet:", item["pet"])
            print("Atividade:", item["atividade"])
            print("Data:", item["data"])
            print("Responsável:", item["responsavel"])
            print("-" * 30)

def acao_atividade():
    while True:
        print("\n1 - Cadastrar atividade")
        print("2 - Listar atividades")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_atividade()
        elif opcao == "2":
            listar_atividades()
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    carregar_txt()
    acao_atividade()
