import pyray
import constants
from players import Players
class VideoService():
    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug
    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()
    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    def draw_players(self, players, centered=False):
        """Draws the given player's text on the screen.
        Args:
            Player (Players): The player to draw.
        """
        text = Players.get_text()
        x = Players.get_position().get_x()
        y = Players.get_position().get_y()
        font_size = Players.get_font_size()
        color = Players.get_color().to_tuple()
        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
        pyray.draw_text(text, x, y, font_size, color)
    def draw_players(self, players, centered=False):
        """Draws the text for the given list of players on the screen.
        Args:
            actors (list): A list of players to draw.
        """
        for player in players:
            self.draw_players(Players, centered)
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """
        pyray.end_drawing()
    def is_window_open(self):
        """Whether or not the window was closed by the user.
        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()
    def open_window(self):
        """Opens a new window with the provided title.
        Args:
            title (string): The title of the window.
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)
    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.BLACK)
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.BLACK)
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)