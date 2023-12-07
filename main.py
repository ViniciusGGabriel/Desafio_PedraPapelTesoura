import random as rd


def vencedor(user, computer):
    if (user == 'Pedra' and computer == 'Tesoura') or (user == 'Tesoura' and computer == 'Papel') or (user == 'Papel' and computer == 'Pedra'):
        return 'Você venceu!'

    return 'Você perdeu!'


def play_game():
    usuario = input(
        "Insira qual valor você escolhe (pedra, papel ou tesoura): 'Pedra', 'Papel' ou 'Tesoura' ")
    # Randomiza os valores de pedra, papel ou tesoura
    computador = rd.choice(['Pedra', 'Papel', 'Tesoura'])
    resultado = vencedor(usuario, computador)
    print(f'Você escolheu {usuario} e o computador escolheu {computador}')
    print(resultado)


play_game()
