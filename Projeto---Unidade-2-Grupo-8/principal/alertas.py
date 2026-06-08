from datetime import datetime

def calcular_dias_restantes(data_tarefa):
    try:
        hoje = datetime.today().date()
        data_convertida = datetime.strptime(
            data_tarefa,
            "%d/%m/%Y"
        ).date()

        return (data_convertida - hoje).days

    except ValueError:
        return None

def cadastrar_tarefa():
    nome = input(
        "Digite o nome do animal: "
    )
    tarefas = []
    quantidade = int(
        input(
            "Quantas tarefas o animal possui? "
        )
    )
    for i in range(quantidade):
        print(f"\nTarefa {i + 1}")

        tipo = input(
            "Digite o nome da tarefa: "
        )
        data = input(
            "Digite a data da tarefa "
            "(DD/MM/AAAA): "
        )
        tarefa = {
            "tipo": tipo,
            "data": data
        }
        tarefas.append(tarefa)

    animal = {
        "nome": nome,
        "tarefas": tarefas
    }
    return animal

def exibir_alertas(animal):
    print(
        f"\n=== ALERTAS DE "
        f"{animal['nome'].upper()} ==="
    )
    for tarefa in animal["tarefas"]:
        dias = calcular_dias_restantes(
            tarefa["data"]
        )
        if dias is None:
            print(
                f"{tarefa['tipo']}: "
                f"data inválida"
            )
        elif dias > 0:
            print(
                f"{tarefa['tipo']}: "
                f"faltam {dias} dias"
            )
        elif dias == 0:
            print(
                f"{tarefa['tipo']}: "
                f"é hoje"
            )
        else:
            print(
                f"{tarefa['tipo']}: "
                f"atrasado há "
                f"{abs(dias)} dias"
            )
animal = cadastrar_tarefa()
exibir_alertas(animal)