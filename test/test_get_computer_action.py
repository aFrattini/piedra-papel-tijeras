import pytest
from src.game import GameAction, get_computer_action


@pytest.mark.agent
def test_computer_picks_paper():
    
    # Restablecer el historial
    if hasattr(get_computer_action, "opponent_history"):
        del get_computer_action.opponent_history
     
    # Simular jugadas
    get_computer_action(GameAction.Rock)
    get_computer_action(GameAction.Rock)
    
    # El agente debería elegir Paper para ganarle a Rock
    result = get_computer_action(GameAction.Rock)
    assert result == GameAction.Paper

@pytest.mark.agent
def test_computer_picks_scissors ():
    
    # Restablecer el historial
    if hasattr(get_computer_action, "opponent_history"):
        del get_computer_action.opponent_history
     
    # Simular jugadas
    get_computer_action(GameAction.Paper)
    get_computer_action(GameAction.Paper)
    
    # El agente debería elegir Scissors para ganarle a Paper
    result = get_computer_action(GameAction.Paper)
    assert result == GameAction.Scissors

@pytest.mark.agent
def test_computer_picks_spock ():
    
    # Restablecer el historial
    if hasattr(get_computer_action, "opponent_history"):
        del get_computer_action.opponent_history
     
    # Simular jugadas
    get_computer_action(GameAction.Scissors)
    get_computer_action(GameAction.Scissors)
    
    # El agente debería elegir Spock para ganarle a Scissors
    result = get_computer_action(GameAction.Scissors)
    assert result == GameAction.Spock


@pytest.mark.agent
def test_computer_picks_lizard ():
    
    # Restablecer el historial
    if hasattr(get_computer_action, "opponent_history"):
        del get_computer_action.opponent_history
     
    # Simular jugadas
    get_computer_action(GameAction.Spock)
    get_computer_action(GameAction.Spock)
    
    # El agente debería elegir Lizard para ganarle a Spock
    result = get_computer_action(GameAction.Spock)
    assert result == GameAction.Lizard


@pytest.mark.agent
def test_computer_picks_rock ():
    
    # Restablecer el historial
    if hasattr(get_computer_action, "opponent_history"):
        del get_computer_action.opponent_history
     
    # Simular jugadas
    get_computer_action(GameAction.Lizard)
    get_computer_action(GameAction.Lizard)
    
    # El agente debería elegir Spock para ganarle a Scissors
    result = get_computer_action(GameAction.Lizard)
    assert result == GameAction.Rock