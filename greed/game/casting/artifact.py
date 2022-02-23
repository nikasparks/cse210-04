from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        
    def get_message(self, item):
        """Gets the artifact's message which is it's point value.
        
        Returns:
            int: The point value.
        """

    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message