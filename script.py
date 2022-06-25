from scores import Scores
from players import Players
Player_I = 0
Player_II = 0
class Script():
    def __init__(self):
        self.players = {}
    def display(self, player):
        """Adds an action to the given player.
        Args:
            score (scores): tally of addends for the totals of player_I and player_II
            Player (execute): The action to add.
        """
        if not player in self.players[Players].keys():
            self.players[self.get_score] = []
        if not player in self.players[self.get_score]:
            self.players[self.get_score].append(player)
    def get_score(self, players):
        """Gets the actions in the given player.
        Args:
            get_score (display_score): to The name of the player.
        Returns:
            List: The additions of the player.
        """
        results = []
        if players in self.players.keys():
            results = self.players[players].copy()
        return results
    def display_scores(self):
        """Removes an action from the given group.
        Args:
            group (string): The name of the group.
            action (Action): The action to remove.
        """
        for player_scores:
            print(f'SCORE: Player_I ={PLAYER_I = SCORE}')
            print(f'SCORE: Player_II ={PLAYER_II = SCORE}')
