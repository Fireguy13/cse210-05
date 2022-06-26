class Scores():
    def __init__(self):
        """Constructs a new Actor."""
        self._points = 0

    def add_points(self, points):
        """Adds the given points to the score's total points.
        Args:
            points (int): The points to add.
        """
        self._points += points

    def get_points(self):
        return self._points

