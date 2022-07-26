# Soccer_Penalty_Calc
GUI allows user to drag soccer ball around goal, and based on several factors like shot speed and goal keeper reaction time, calculates whether the shot will be saved or not. (Python)


Project split into two classes: image.py and soccer.py

1) Image.py runs the program and create the GUI using pygame

2) Soccer.py performs the calculations pertaining to whether or not the goalkeeper will have sufficient time to save the shot.
  -user may alter shot location, shot speed, goal keeper reaction time to acheive desired shot profile


As the user drags the soccer ball to new locations around the goal, the program will output three different scenarios:

1) Soccer Ball Outlined in RED

If the ball's outline is red, no calculation will be performed, as either the shot will be instantly saved (giving the goalkeeper no need to dive), or the ball is not on target (perhaps over the goal)

![Red](https://user-images.githubusercontent.com/102982612/181078694-e6639411-cf82-4c14-b497-49796f6d3613.png)

![Out](https://user-images.githubusercontent.com/102982612/181079413-e35ccd03-fd96-4ee6-b195-2a63372a562b.png)


2) Soccer Ball Outlined in GREEN

If the ball's outline is green, then the goalkeeper does not have enough time to reach the ball, and no matter the reaction time, will not be able to save the shot (most common scenario for any of the four corners)

![Green](https://user-images.githubusercontent.com/102982612/181078957-39e97a9e-8184-4a7f-9712-2346d2772289.png)


3) Lastly if the soccer ball's outline is orange, it may be possible for the goalkeeper to save the ball (aka if the goalkeeper reacts within reasonable time, he will block the ball before it goes in). In this case, at the bottom of the screen, the program will display how much time the keeper has to react, if he wants to save the ball in time.

![Orange](https://user-images.githubusercontent.com/102982612/181079382-581ea4ae-f547-4db2-91de-c71b12ef1c4c.png)


This project was submitted to the college board, as part of the AP Computer Science Principles exam. The score received was a 5 (awarded to the top 10.8% of test takers).
