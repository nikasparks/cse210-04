import os
import random
import time

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60   # Columns * cell size = MAX_X
ROWS = 40   # Rows * cell size = MAX_Y
CAPTION = "Greed"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40   # The number of stones and gems distributed across the screen


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2) 
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    # with open(DATA_PATH) as file:
    #     data = file.read()
    #     messages = data.splitlines()

<<<<<<< HEAD
    for n in range(DEFAULT_ARTIFACTS):
        
        text = chr(random.choice([42, 48]))
        #message = messages[n]
=======
    # for n in range(DEFAULT_ARTIFACTS):
            
    #     text = chr(random.choice([42, 48]))  #Use only squares and asterisks for artifact shapes
    #     # message = messages[n]
>>>>>>> 582945bfc4000b03afb2e0a8386234e6cc26d582

    #     x = random.randint(1, COLS - 1)  #Distribute artifacts randomly across the screen horizontally
    #     # y = random.randint(1, ROWS - 1)  #Distribute artifacts randomly in vertical spacing, this is for RFK, not for Greed
    #     y = 1  # For Greed, need to start y at the top row
    #     position = Point(x, y)
    #     position = position.scale(CELL_SIZE)

    #     r = random.randint(10, 255)
    #     g = random.randint(10, 255)
    #     b = random.randint(10, 255)
    #     color = Color(r, g, b)
            
    #     artifact = Artifact()
    #     artifact.set_text(text)
    #     artifact.set_font_size(FONT_SIZE)
    #     artifact.set_color(color)
    #     artifact.set_position(position)
    #     # artifact.set_message(message)
    #     cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()