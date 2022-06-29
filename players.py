

from constants import GREEN, RED, WHITE, COLUMNS, ROWS, GROW_ON_TURN
from point import Point
from scores import Scores
from snake import Snake

class Players:
    score = Scores()
    snake = None
    grow_segments = 0
    score_x = 0
    score_y = 0
    def __init__(self, initial_segment_list):
        '''makes up the workings of the green and red 
        snakes upon the screen that the video_service 
        displays:'''
        self._up = None
        self._down = None
        self._left = None
        self._right = None
        self.snake = Snake(initial_segment_list)

    def set_direction(self, direction):
        if direction != self.snake.get_direction():
            # We turned, increment the number of segments we need to grow
            self.grow_segments += GROW_ON_TURN
        self.snake.set_direction(direction)

    def set_movement_keys(self, up, down, left, right):
        self._up = up
        self._down = down
        self._right = right
        self._left = left
    
    def is_left_key(self, key):
        if key == self._left:
            return True
        return False
    
    def is_right_key(self, key):
        if key == self._right:
            return True
        return False
    
    def is_up_key(self, key):
        if key == self._up:
            return True
        return False
    
    def is_down_key(self, key):
        if key == self._down:
            return True
        return False

    def get_movement_keys(self):
        return self._up, self._down, self._left, self._right

    def move_next(self):
        """
        moves the snake once in the current direction.  Only call this when the snake
        should move. Velocity is determined by how frequently you call this function,
        nothing else.  This only considers direction.
        """
        # Move the head in the current direction
        prev_position = Point(self.snake.get_segments()[0].get_x(), self.snake.get_segments()[0].get_y())
        tail =  Point(self.snake.get_segments()[-1].get_x(), self.snake.get_segments()[-1].get_y())
        head = self.snake.get_segments()[0]
        if self.snake._direction.get_x() + head.get_x() >= COLUMNS:
            head.set_x(0)
        elif self.snake._direction.get_x() + head.get_x() <= 0:
            head.set_x(COLUMNS)
        elif self.snake._direction.get_y() + head.get_y() >= ROWS:
            head.set_y(0)
        elif self.snake._direction.get_y() + head.get_y() <= 0:
            head.set_y(ROWS)
        else:
            head.add(self.snake._direction)        
        # rest of the body follows the head by moving into the space vacated by the previous 
        # body part
        for i in range(1,len(self.snake.get_segments())):
            next_prev_pos = Point(self.snake.get_segments()[i].get_x(), self.snake.get_segments()[i].get_y())
            self.snake.get_segments()[i].set_x(prev_position.get_x())
            self.snake.get_segments()[i].set_y(prev_position.get_y())
            prev_position = next_prev_pos
        
        if self.grow_segments > 0:
            # add one extra segment on the tail if we need to grow
            self.snake.grow_tail(tail)
            self.grow_segments -= 1

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self.snake.color = color

    def get_color(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The actor's text color.
        """
        return self.snake.color
