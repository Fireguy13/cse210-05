import constants
from point import Point
from contestants import Contestants
import constants

class Snake(Contestants):
    """
    A long limbless reptile.
    The responsibility of Snake is to move itself.
    Attributes:
        _points (int): The number of points the food is worth.
    """
    color = constants.WHITE
    _segments = []
    _direction = None
    
    def __init__(self, initial_segment_list):
        # initial segment list is a list of points that represents 
        # the initial body segment positions
        self._segments = initial_segment_list
    
    def set_direction(self, direction):
        self._direction = direction

    def get_direction(self):
        return self._direction
        
    def get_segments(self):
        return self._segments

    def get_head(self):
        return self._segments[0]
    
    def grow_tail(self, point):
        self._segments.append(point)
    
