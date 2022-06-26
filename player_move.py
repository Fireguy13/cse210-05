from execution import Execution

class PlayerMove(Execution):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def __init__(self, player):
        self._player = player
        
    def execute(self):
        """Executes the player's move"""
        self._player.move_next()
