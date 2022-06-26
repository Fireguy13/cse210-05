from tkinter import CENTER
from point import Point
import constants
from players import Players
from contestants import Contestants
from direction import Direction
from scores import Scores
class Collision(Point):    

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
#add the fusin back
    def execute(self, contestants, script): 
        """Executes the handle collisions action.
        Args:
            contestants (Players): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_collision(Contestants)
            self._handle_segment_collision(Contestants)
            self._handle_game_over(Contestants)

    def _handle_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        #look at this it is the same collision_det
        Scores = Players.get_move_next("scores")
        
        snake = Players.get_move_next("")
        head = snake.get_head()

        
        points = Direction.get_points()
        #add2 add when it moves     snake.grow_tail(points)
           #add 2  score.add_points(points)
            
    def _handle_segment_collision(self, contestants):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        snake = contestants.get_move_next("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, contestants):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = contestants.get_move_next("snakes")
            segments = snake.get_segments()
            food = contestants.get_move_next("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Players()
            message.set_text("Game Over!", CENTER)
            message.set_position(position)
            contestants.add_player("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            Players.set_color(constants.WHITE)
