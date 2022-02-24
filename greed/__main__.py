from imaplib import Int2AP
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

# Setup constants
FRAME_RATE = 7
MAX_X = 1200
MAX_Y = 900
CELL_SIZE = 30
FONT_SIZE = 30
COLS = int(MAX_X/CELL_SIZE)   # Columns * cell size = MAX_X
ROWS = int(MAX_Y/FONT_SIZE)     # Rows * cell size = MAX_Y
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 50
message = 0

def main():
    global message
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
    y = int(MAX_Y-CELL_SIZE) 
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    #create Gems(*) and Rocks(O)
    for n in range(DEFAULT_ARTIFACTS):
        #randomly create a gem or a rock
        char_text = [42, 79]
        symbol = random.choice(char_text)
        text = chr(symbol)
        #give it a point value
        if symbol == 42:
            message = 1
        elif symbol == 79:
            message = -1
        #set starting point
        x = random.randint(1, COLS - 1)
        y = random.randint(1, int(ROWS/7))
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        #set color
        r = random.randint(40, 250)
        g = random.randint(40, 250)
        b = random.randint(40, 250)
        color = Color(r, g, b)
        #store in artifacts group
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service, CELL_SIZE, COLS, ROWS)
    director.start_game(cast)


if __name__ == "__main__":
    main()