import pyray 
import random
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
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
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

    def advance(self):
            self.position.y += self.velocity.dy
            self.position.x += self.velocity.dx

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

        
        for artifact in artifacts:
            art_v_x = artifact._position.get_x()
            art_v_y = (random.randint(1,3)*15)
            art_vel = (art_v_x,art_v_y)
            artifact.set_velocity(art_vel)
            # artifact.move_down(1,max_y)
            artifact.move_next(max_x, max_y)


            if robot.get_position().equals(artifact.get_position()):
                #score calc
                point = artifact.get_message()                                  
                self._score += point
                #self._score = artifact.get_message(score)
                artifact.set_position((random.randint(1,59)*15),(random.randint(1,3)*15))
                artifact.move_next(max_x, max_y)
            # if artifact._position.get_y() >= max_y:
            #     artifact.move_next((random.randint(1,59)*15),random.randint(-3,-1)*15)    

        banner.set_text(f"Score: {self._score}")

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()