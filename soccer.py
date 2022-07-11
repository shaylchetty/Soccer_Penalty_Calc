import math


def Calculate(x, y, shot_speed, goalie_reaction_time):

    global Color

    x += 0.75  # adjusted for positioing of goalie in image
    y += -3
    # x-coordinate of shot
    # x = abs(float(input("Enter the X coordinate of the shot: ")))
    # y = abs(float(input("Enter the Y coordinate of the shot: ")))
    goalie_full_reach = 7.5
    goalie_jump_speed = 10  # feet per second
    # check if shot is on target

    if (x > 12 or y > 8):
        print("The current shot is not on target")
        Color = "Red"

    # distance from goalie to ball location in goal
    goalie_ball_distance = math.sqrt(
        (x**2 + y**2)) - goalie_full_reach/2  # adjusted for goal keeper reach
    if(goalie_ball_distance < 0):
        Color = "Red"
        return(
            "No time needed for reaction; the ball is within the goalie's diving envelope!")

    # time it takes for keeper to reach the goal
    goalie_time_to_ball = goalie_ball_distance/goalie_jump_speed

    # distance from penalty spot to shot location
    ground_distance = math.sqrt(x ** 2 + 1296)
    shot_distance = math.sqrt(ground_distance ** 2 + y ** 2)

    # time it takes for ball to reach the goal
    ball_time_to_goal = shot_distance/shot_speed

    goalie_time_to_react = round(ball_time_to_goal - goalie_time_to_ball, 2)

    if goalie_time_to_react < goalie_reaction_time:
        Color = "Green"
        return(
            "There is not enough time for the goalie to save the ball!")
    else:
        Color = "Orange"
        return (f"The Goalie has {goalie_time_to_react} seconds to react!")


Color = ""

Calculate(13, 8, 60, 0.15)
