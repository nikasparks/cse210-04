import random
import time
from game.casting.artifact import Artifact
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.shared.color import Color
from game.shared.point import Point

class Director:
     
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """
    
    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        cast = Cast()
        self._score = 0     #created overall score to be displayed and updated in methods
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._create_shapes(cast)  # creating a method that will repetitively create shapes
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _create_shapes(self, cast):
        text = chr(random.choice([42, 48]))  #Use only squares and asterisks for artifact shapes  
        x = random.randint(1, 60 - 1)  # Distribute artifacts randomly across the screen horizontally, 
                                        # hard coding COLS here to be 60, can use constant or parameter later
        y = 1  # For Greed, need to start y at the top row
        position = Point(x, y)
        position = position.scale(15) # hard coding cell size to be 15 here, can use a parameter or constant later

        # stones and gems will have random colors
        r = random.randint(10, 255)
        g = random.randint(10, 255)
        b = random.randint(10, 255)
        color = Color(r, g, b)
            
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(15) # hard coding font size to be 15 here, can use a parameter or constant later
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor("artifacts", artifact)
    
    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        score = 0
        for artifact in artifacts:
            
            if robot.get_position().equals(artifact.get_position()):
                # create score calc                                   
                score += 1
        
                #score = artifact.get_message(score)
                #banner.set_text(score)
        pyray.draw_text(f"score {score}",10 , 0, 15, pyray.WHITE)
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()