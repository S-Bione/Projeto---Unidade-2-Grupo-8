from datetime import datetime


def calcular_dias_restantes(data_tarefa):
    try:
        hoje = datetime.today().date()
        data_convertida = datetime.strptime(data_tarefa, "%d/%m/%Y").date()
        return (data_convertida - hoje).days
    except ValueError:
        return None


def exibir_alertas(animal):
    print(f"\n=== ALERTAS DE {animal['nome'].upper()} ===")

    for tarefa in animal["tarefas"]:
        dias = calcular_dias_restantes(tarefa["data"])

        if dias is None:
            print(f"{tarefa['tipo']}: data inválida")

        elif dias > 0:
            print(f"{tarefa['tipo']}: faltam {dias} dias")

        elif dias == 0:
            print(f"{tarefa['tipo']}: é hoje")

        else:
            print(f"{tarefa['tipo']}: atrasado há {abs(dias)} dias")


animal = {
    "nome": "Rex",
    "tarefas": [
        {"tipo": "Vacina V10", "data": "20/06/2026"},
        {"tipo": "Consulta veterinária", "data": "08/06/2026"},
        {"tipo": "Banho", "data": "01/06/2026"}
    ]
}


