import random
from enum import IntEnum
from collections import Counter


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}


def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # User picked Rock
    elif user_action == GameAction.Rock:
        if computer_action in [GameAction.Scissors, GameAction.Lizard]:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You won!")
            game_result = GameResult.Victory
        else:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You lost!")
            game_result = GameResult.Defeat

    # User picked Paper
    elif user_action == GameAction.Paper:
        if computer_action in [GameAction.Rock, GameAction.Spock]:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You won!")
            game_result = GameResult.Victory
        else:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You lost!")
            game_result = GameResult.Defeat

    # User picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action in [GameAction.Paper, GameAction.Lizard]:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You won!")
            game_result = GameResult.Victory
        else:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You lost!")
            game_result = GameResult.Defeat
    
    # User picked Lizard
    elif user_action == GameAction.Lizard:
        if computer_action in [GameAction.Spock, GameAction.Paper]:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You won!")
            game_result = GameResult.Victory
        else:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You lost!")
            game_result = GameResult.Defeat
    
    # User picked Spock 
    elif user_action == GameAction.Spock:
        if computer_action in [GameAction.Scissors, GameAction.Rock]:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You won!")
            game_result = GameResult.Victory
        else:
            print(f"You picked {user_action.name} and the computer picked {computer_action.name}. You lost!")
            game_result = GameResult.Defeat

    return game_result


def get_computer_action(user_action):

    # Inicializar el historial solo una vez
    if not hasattr(get_computer_action, "opponent_history"):
        get_computer_action.opponent_history = [] 

    # Actualizar el historial de jugadas
    get_computer_action.opponent_history.append(user_action)
    
    # Contar las 10 últimas jugadas del oponente y buscar la más comun
    recent_history = get_computer_action.opponent_history[-10:] 
    move_counts = Counter(recent_history)
    most_common_move = move_counts.most_common(1)[0][0]

    # Elegir la jugada que gana contra la jugada más común
    if most_common_move == GameAction.Rock:
        computer_action = GameAction.Paper
    elif most_common_move == GameAction.Paper:
        computer_action = GameAction.Scissors
    elif most_common_move == GameAction.Scissors:
        computer_action = GameAction.Spock
    elif most_common_move == GameAction.Spock:
        computer_action = GameAction.Lizard
    else:
        computer_action = GameAction.Rock
    
   
    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(user_action)
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()