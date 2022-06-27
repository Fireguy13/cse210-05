import constants
from script import Script
from scores import Scores
from snake import Snake
from collision import Collision
from draw_players_action import DrawPlayersAction
from director import Director
from direction import Direction
from keyboard_service import KeyboardService
from script import Script
from constants import RED, GREEN
from video_service import VideoService
from execution import Execution
from contestants import Contestants
from players import Players
from colors import Colors
from point import Point
def main():
    # create the cast
    player1_initial_snake_body = []
    for i in range(8):
        player1_initial_snake_body.append(Point(20,i+20))
    player2_initial_snake_body = []
    for i in range(8):
        player2_initial_snake_body.append(Point(60,i+20))
    player1 = Players(player1_initial_snake_body)
    player1.set_movement_keys('w','s','a','d')
    player2 = Players(player2_initial_snake_body)
    player2.set_movement_keys('i','k','j','l')
    # a list of players could be stored somewhere like in the director
    player1.snake.color = RED
    player1.snake.set_direction(Direction((1,0)))
    player2.snake.color = GREEN
    player2.snake.set_direction(Direction((1,0)))
    contestants = Contestants([player1,player2])
    # something you would do later when you hit an event that effects your score
    #player1.score.add_points(1)
    #player2.score.add_points(1)
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    script = Script()
    '''
    script.add_direction("input", Direction(keyboard_service))
    script.add_direction("update",DrawPlayersAction())
    script.add_direction("update", CollisionDetection())
    script.add_direction("output", DrawPlayersAction(video_service))
    '''
    director = Director(video_service)
    director.start_game(contestants, script)
    
if __name__ == "__main__":
    main()




