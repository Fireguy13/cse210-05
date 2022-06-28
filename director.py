
from execution import Execution
from time import sleep
from keyboard_service import KeyboardService
import constants
from collision_detection import CollisionDetection
from players import Players
from scores import Scores
from script import Script
from contestants import Contestants
from snake import Snake
from player_move import PlayerMove
from video_service import VideoService


class Director():
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """
    _video_service = None
    player1_score = 0
    player2_score = 0
    #initiates the game and the first action taking place 
    # makes sure all things are being added to the video_service too.
    def __init__(self, video_service, script):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._keyboard_service = KeyboardService()
        self._collision_detection = None
        self.script_score = script

    def start_game(self, contestants):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        self._collision_detection = CollisionDetection(contestants)
        self._video_service.open_window()
        
        move_at = 1/constants.MOVEMENTS_PER_SECOND
        time_since_last_move = 0.0
        while self._video_service.is_window_open():
            self._video_service.clear_buffer()
            self._keyboard_service.set_direction_for_contestants(contestants)
            actions = []
            if time_since_last_move >= move_at:
                for player in contestants.get_players():
                    actions.append(PlayerMove(player))
                time_since_last_move = 0
            if self._collision_detection == True:
                # find any collision actions and append them to the actions list
                if contestants.get_players[0].score.get_points() > contestants.get_players[1].score.get_points():
                    print('Player 1 wins!\n GAME OVER!')
                if  contestants.get_players[0].score.get_points() < contestants.get_players[1].score.get_points():
                    print('Player 2 wins!\n GAME OVER!')
                else:
                    print('Score is a TIE!\n GAME OVER!') 
                return
            #self.update_scores.get_points()+ self.update_scores.add_points() == self.updated_scores 
            #self.script_score.display_scores(self._video_service)
            for action in actions:
                action.execute()
            self._video_service.draw_players(contestants.get_players())
            self._video_service.flush_buffer()
            time_since_last_move += 1/constants.FRAME_RATE
            sleep(1/constants.FRAME_RATE)
                    
        self._video_service.close_window()
        return

    def execute(self, execute_type, players, script):
        """Calls execute for each players script.
        
        Args:
            Players (player_1 or player_2): The action group name.
            script (Script): The script off additions and text display
            for the contestants progress or defeat.
        """
        #score = script.get_score()    
        #while score == players.player_1:
        #    script.get_scores.execute(players, script)
        #    if score == players.player_2:
        #       script.get_scores.execute(players, script)


