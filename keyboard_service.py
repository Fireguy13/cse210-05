import pyray
from point import Point
from direction import Direction

class KeyboardService():
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def set_direction_for_contestants(self, contestants):
        # detect the current keys being pressed and
        # determine if they are any of the players movement keys
        # if they are set the direction on all the players who 
        # have pressed movement keys. 
        for player in contestants.get_players():
            for char in player.get_movement_keys():
                if self.is_key_down(char):
                    if player.is_up_key(char):
                        player.set_direction(Direction((0,-1)))
                    elif player.is_down_key(char):
                        player.set_direction(Direction((0,1)))
                    if player.is_right_key(char):
                        player.set_direction(Direction((1,0)))
                    elif player.is_left_key(char):
                        player.set_direction(Direction((-1,0)))

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        return pyray.is_key_down(self._keys[key])
    
    
