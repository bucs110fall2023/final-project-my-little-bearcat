[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803369&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Bearcat Jump
## CS110 Final Project  Fall, 2023

## Team Members

Allison Jenkins, David Fayle

***

## Project Description

We adjusted our project, modeling it after the classic "Doodle Jump" game. Long long ago, back in the 2010s, we both distinctly remember tapping and moving the Doodle figure around the screen of our parent's phone, hoping to beat our previous high score. We decided to recreate this nostalgia and make it our own. Enjoy "Bearcat Jump"!!!

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui1.jpg)
![final gui](assets/finalgui2.jpg)
![final gui](assets/finalgui3.jpg)

## Program Design

### Features

1. Menu Options
2. Random Platforms
3. Doodle Jumping
4. Doodle moving left and Right
5. Doodle Flips Direction
6. A "best time" functionality

### Classes

The Baseplatform Class = Baseplatform.py: Perhaps our most simple class, we initialized the class to create a "grounding" for our Bearcat.

The BestTime Class = BestTime.py: In this class, we developed methods for our game to display a "Best Time", satisfying the data permeance objective.

The Button Class - Button.py: In the Button class, we created a method to actually draw the button, and then also a method that allows the user to click said button.

The Doodle Class - Doodle.py: In this class, we are able to create a "bearcat" that acts as our doodle in the game. We also created the methods for gravity, jumping, and and update method including our collision code.

The Platforms Class = Platforms.py: In this class, we created a method to create the platforms, and also wrote code to make the platforms appear randomly in the window.

The Springs Class - Springs.py: Hopefully, we will be able to code more in the Springs class in the coming days.

## Modules Used and Data Permanence

While of course we used pygame, we also imported "time" in order to keep track of the time it took to reach the top, "os" in order to manage the files we created and "sys" for general operations of the program.

To satisfy the Data Permanence aspect of the project, we have a "Best Time" feature that retrieves and stores the lowest time it has taken the user to reach the top of the screen that is loaded in the top left and replaced if necessary.

## Class Diagram/Description

Baseplatform: self, width, height, color
- image: The visual representation of the platform.
- rect: The rectangular area occupied by the platform.

Button: self, width, height, color, text
- x: Top left corner coordinates on the x-axis.
- y: Top left corner coordinates on the y-axis.
- width: Width of the button.
- height: Height of the button.
- color: Color of the button.
- text: Text displayed on the button.

Controller: self, x, y ***MANAGES THE GAME!!!***
- x: Width of the window.
- y: Height of the window.

Doodle: self, base_platform, platforms
- base_platform: The ground where the Doodle stands.
- platforms: Platforms where the doodle can jump.

Platforms: self, x, y, width, height, color
- width: Width of the platform.
- height: Height of the platform.
- image: Visual of the platform.
- rect: The rectangular are the platform takes up on the screen.

Timer: self
- start_time: Time when timer is started.
- end_time: The time when the timer is stopped.
- highest_score: The elapsed time.
    
## ATP

| Step | Action | Result|

|1  | Run the main.py code. | This should trigger the game window to appear. |

|2  | Click the "Quit" Button | This will cause the game window to close. |

|3  | Click the "Start Game" Button. | This will cause the game to commence. |

|4  | Using the keyboard press "A" or "D". | This will move the Bearcat to the left or right, respectively. |

|5  | Press Spacebar. | This will move the Bearcat up smoothly. |

|6  | Land on a platform utilizing steps 4 and 5 | This will cause the Bearcat to "land" on a platform. |

|7  | Reach the top (y=0) | This will end the game and stop the timer, it will display the reset screen |

|8  | Press "Reset" | This will restart the game while also displaying the lowest time it took to reach the top |

|9  | Press "Menu" | This will redirect the user to the opening display that contains the "Start Game" and "Quit" buttons |