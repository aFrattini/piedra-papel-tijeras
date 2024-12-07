from src.game import GameAction, get_computer_action

def test_computer_action_rock ():
    
    # Restablecer el historial
    if hasattr(get_computer_action, "opponent_history"):
        del get_computer_action.opponent_history
     
    # Jugadas mayormente Piedra
    get_computer_action(GameAction.Rock)
    get_computer_action(GameAction.Rock)
    
    # El agente debería elegir Papel para ganarle a la Piedra
    result = get_computer_action(GameAction.Rock)
    assert result == GameAction.Paper


def test_computer_action_paper ():
    
    # Restablecer el historial
    if hasattr(get_computer_action, "opponent_history"):
        del get_computer_action.opponent_history
     
    # Jugadas
    get_computer_action(GameAction.Paper)
    get_computer_action(GameAction.Paper)
    
    # El agente debería elegir Tijeras para ganarle al papel
    result = get_computer_action(GameAction.Paper)
    assert result == GameAction.Scissors


def test_computer_action_scissors ():
    
    # Restablecer el historial
    if hasattr(get_computer_action, "opponent_history"):
        del get_computer_action.opponent_history
     
    # Jugadas
    get_computer_action(GameAction.Scissors)
    get_computer_action(GameAction.Scissors)
    
    # El agente debería elegir Piedra para ganarle a las Tijeras
    result = get_computer_action(GameAction.Scissors)
    assert result == GameAction.Rock