from abc import ABCMeta, abstractmethod
from keyboard_service import KeyboardService

class Execution(metaclass=ABCMeta):
    # Abstract base class for multiple action types in the game.  
    def __init__(self):
        pass
        
    @abstractmethod
    def execute(self):
        # this is the abstract base class you will not implement 
        # anything for execute here.  Any class that inherits from
        # Execution will need to have an execute method, with details
        # on what execute means and does for that inherited class.
        pass
