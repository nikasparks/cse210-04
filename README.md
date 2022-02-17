# Greed Game for CSE 210

## Status: in progress

## Description:
- Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more! This project was created for CSE 210 at BYU Idaho.

## Project Structure:
- geed: folder housing all the parts for the game and where the __ main__.py and game design file live.
- __ main__.py: contains our main function utilizing the classes in different files and builds the game window definitions for video_service.py to use in drawing the game.
- game: a folder containing the files for the game to run.
- casting: a folder containing the files for the to create the different interactive pieces of the game.
- directing: a folder containing the files to direct the game including director.py.
- services: a folder containing the files that show and receive information from the user.
- shared: a folder containing the utility files for the any class to use in the game.
- director.py: a file containing all info relating to the "Director" class.
- keyboard_service.py: a file that intereprets user's keyboard input using the "KeyboardService" class.
- video_service.py: a file that draws the game window and shows the user any information they need using the "VideoService" class.
- 
- 
- 
- 
- 

## Technologies Used:
- The only software required for this program is Python. You can download it here: https://www.python.org
- The collaboration was done via github: https://github.com/nikasparks/cse210-04.git

## Game Instructions:
- Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
- The player (#) can move left or right along the bottom of the screen.
- If the player touches a gem they earn a point.
- If the player touches a rock they lose a point.
- Gems and rocks are removed when the player touches them.
- The game continues until the player closes the window.

## Acknowledgements:
- Camron Erickson: eri20010@byui.edu
- Monika Meyers: nikasparks@mac.com
- Jonathan Woster: jonathanwoster@gmail.com
- Arnaldo Suarez: sua21007@byui.edu