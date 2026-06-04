def sugestao(animal):
    especie = animal[1].lower()
    idade = int(animal[3])
    comportamento = animal[6].lower()

    print("\n===== SUGESTÃO DE ADOÇÃO =====")

    if especie == "cachorro" and "brinc" in comportamento:
        print("Ideal para famílias com crianças.")

    elif especie == "gato":
        print("Indicado para apartamentos.")

    if idade <= 1:
        print("Filhote: necessita mais atenção.")

    elif idade >= 8:
        print("Animal idoso: ambiente tranquilo.")

def mostrar_sugestoes():
    animais = carregar_animais()

    if len(animais) == 0:
        print("Nenhum animal cadastrado.")
        return

    listar_animais()

    indice = int(input("\nEscolha o número do animal: ")) - 1

    if 0 <= indice < len(animais):
        sugestao(animais[indice])
    else:
        print("Animal não encontrado.")