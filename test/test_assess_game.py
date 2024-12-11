import pytest
from src.game import GameResult, GameAction, assess_game

@pytest.mark.draw
def test_draw():
    '''
    Tied games
    '''

    assert GameResult.Tie == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Rock)

    assert GameResult.Tie == assess_game(
        user_action=GameAction.Scissors, 
        computer_action=GameAction.Scissors)

    assert GameResult.Tie == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Paper)
    
    assert GameResult.Tie == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Spock)
    
    assert GameResult.Tie == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Lizard)
    
@pytest.mark.rock
def test_rock_loses():
    '''
    User picked rock and loses
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Paper)
    
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Spock)

@pytest.mark.rock
def test_rock_wins():
    '''
    User picked rock and wins 
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Scissors)
    
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Lizard)



@pytest.mark.paper
def test_paper_loses():
    '''
    User picked Paper and loses 
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Scissors)
    
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Lizard)

@pytest.mark.paper
def test_paper_wins():
    '''
    User picked Paper and wins
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Rock)
    
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Spock)

@pytest.mark.scissors
def test_scissors_loses():
    '''
    User picked Scissors and loses
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Rock)

    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Spock)
    
@pytest.mark.scissors
def test_scissors_wins():
    '''
    User picked Scissors and wins
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Paper)

    assert GameResult.Victory == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Lizard)
    
@pytest.mark.lizard
def test_lizard_loses():
    '''
    User picked Lizard and loses
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Rock)
    
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Scissors)

@pytest.mark.lizard
def test_lizard_wins():
    '''
    User picked Lizard and wins 
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Paper)

    assert GameResult.Victory == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Spock)
    

@pytest.mark.spock
def test_spock_loses():
    '''
    User picked Spock and loses
    '''
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Lizard)
    
    assert GameResult.Defeat == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Paper)

@pytest.mark.spock
def test_spock_wins():
    '''
    User picked Spock and wins 
    '''
    assert GameResult.Victory == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Scissors)

    assert GameResult.Victory == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Rock)