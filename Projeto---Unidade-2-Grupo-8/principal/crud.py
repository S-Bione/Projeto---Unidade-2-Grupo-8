import os

dados = {}
i=0 

caminho = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "dados",
    "cadastro.txt"
)

def cadastro():
    global i
    i+=1
    pet = {}

    pet["ID do pet"] = i
    pet["Nome"] = input("Nome do pet: ")
    pet["Espécie"] = input("Espécie do pet: ")
    pet["Raça"] = input("Raça do pet: ")
    pet["Idade"] = int(input("Idade do pet: "))
    pet["Estado de saúde"] = input("Estado de saúde do pet: ")
    pet["Data de chegada"] = input("Data de chegada do pet: ")
    pet["Comportamento"] = input("Comportamento do pet: ")

    dados[i] = pet
    salvar_dados()

def salvar_dados():
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for id_pet, pet in dados.items():
            arquivo.write(f"ID: {id_pet}\n")
            arquivo.write(f"Nome: {pet['Nome']}\n")
            arquivo.write(f"Espécie: {pet['Espécie']}\n")
            arquivo.write(f"Raça: {pet['Raça']}\n")
            arquivo.write(f"Idade: {pet['Idade']}\n")
            arquivo.write(f"Estado de saúde: {pet['Estado de saúde']}\n")
            arquivo.write(f"Data de chegada: {pet['Data de chegada']}\n")
            arquivo.write(f"Comportamento: {pet['Comportamento']}\n")
            arquivo.write("-" * 30 + "\n")

def excluir():
    id_excluido = int(input("ID do pet que deseja excluir: "))
    
    if id_excluido not in dados:
        print("ID inválido.")
    else:
        dados.pop(id_excluido)
    salvar_dados()

def editar():
    id_editar = int(input("ID do pet que deseja editar: "))

    if id_editar in (dados):
        pet = dados[id_editar]

        editar_item = input("Qual item deseja editar?")
    
        if (editar_item == "Nome"):
            pet["Nome"] = input("Nome do pet: ")
    
        elif (editar_item == "Espécie"):
            pet["Espécie"] = input("Espécie do pet: ")

        elif (editar_item == "Raça"):
            pet["Raça"] = input("Raça do pet: ")

        elif (editar_item == "Idade"):
            pet["Idade"] = int(input("Idade do pet: "))

        elif (editar_item == "Estado de saúde"):
            pet["Estado de saúde"] = input("Estado de saúde do pet: ")

        elif (editar_item == "Data de chegada"):
            pet["Data de chegada"] = input("Data de chegada do pet: ")

        elif (editar_item == "Comportamento"):
            pet["Comportamento"] = input("Comportamento do pet: ")
        
        salvar_dados()
        
    else:
        print("ID inválido.")
 
def acao():
    print("1 - Cadastrar pet\n2 - Excluir pet\n3 - Editar pet")
    opcao = int(input("Oque deseja realizar: "))

    if (opcao == 1):
        cadastro()
    
    elif (opcao == 2):
        excluir()
    
    elif (opcao == 3):
        editar()

acao()

def repeticao():
     while True:
        repetir = input("Deseja realizar mais algum cadastro ou alteração? ").title()
    
        if (repetir == "Sim" or repetir == "S"):
            os.system('cls' if os.name == 'nt' else 'clear')
            acao()

        elif (repetir == "Não" or repetir == "N" or repetir == "Nao"):
            print("Obrigado!")
            break

repeticao()
