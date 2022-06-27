from point import Point

class Direction():
    valid_directions = [(-1,0), (0,-1), (+1,0), (0,+1)]
    _direction = None
    def __init__(self, initial_direction):
        self.set_direction(initial_direction)
    
    def validate_direction(self, dir):
        if dir not in self.valid_directions:
            raise Exception("Invalid direction")

    def set_direction(self, direction):
        self.validate_direction(direction)
        self._direction = direction
    
    def get_x(self):
        return self._direction[0]
    
    def get_y(self):
        return self._direction[1]
