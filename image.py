import pygame
from pygame.locals import *
import soccer
import pygame.font
import time


def overlap(srect, lrect):
    if(srect.center[0] > lrect.bottomleft[0] and srect.center[0] < lrect.bottomright[0] and srect.center[1] < lrect.bottomleft[1] and srect.center[1] > lrect.topleft[1]):
        return True
        # if(srect.center[1] > lrect.bottomleft[1] and srect.center[1] < lrect.topleft[1]):

    return False


def getxy(rect):
    # get x and y coordinates of the ball
    x = rect.center[0]
    y = rect.center[1]

    x = (x-631.5)/36.5
    y = -(y-500)/37.5
    if (y < -0.05 or y > 8.05):
        return -1, -1
    elif (x > 12.05 or x < -12.05):
        return -1, -1

    else:
        return round(x), round(y)


def text():
    my_string = soccer.Calculate(x, y, 60, 0.25)
    text = font.render(my_string, True, (255, 0, 0))
    screen.blit(text, text.get_rect(
        center=(screen.get_rect().center[0], screen.get_rect().center[1] + 350)))
    pygame.display.flip()


# Take colors input
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Construct the GUI game
pygame.init()

# Set dimensions of game GUI
w, h = 1200, 800
screen = pygame.display.set_mode((w, h))
bg = pygame.image.load(
    "Soccer/goalkeeper-standing-in-goal-ISF00492.jpeg")
# Take image as input
img = pygame.image.load(
    'Soccer/8-86956_soccer-ball-transparent-background-png-transparent-background-soccer (1).png')
img = pygame.transform.scale(img, (35, 35))
img.convert()

# Draw rectangle around the image
rect = img.get_rect()

rect.center = 631.5, 650

# Set running and moving values
running = True
moving = False

rectangle = pygame.rect.Rect(193, 200, 877, 300)  # change 30 to 300

Color = "Red"
new_Color = Color
prev_Color = Color
# Setting what happens when game
# is in running state

# Set screen color and image on screen


while running:
    pygame.draw.rect(screen, BLUE, rectangle)
    screen.blit(bg, (0, 0))
    screen.blit(img, rect)
    pygame.draw.rect(screen, Color, rect, 2)
    font = pygame.font.SysFont("American Typewriter", 25)



# now print the text

    for event in pygame.event.get():
        new_Color = Color
        if (new_Color != prev_Color):
            pygame.draw.rect(screen, Color, rect, 2)
        prev_Color = Color
        # Close if the user quits the
        # game
        if event.type == QUIT:
            running = False

        # Making the image move
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        # Set moving as False if you want
        # to move the image only with the
        # mouse click
        # Set moving as True if you want
        # to move the image without the
        # mouse click
        elif event.type == MOUSEBUTTONUP:
            x, y = getxy(rect)
            if(x != -1 or y != -1):
                text()
            moving = False

        # Make your image move continuously
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

        if(overlap(rect, rectangle)):
            # Color = "Green"
            Color = soccer.Color
        else:
            Color = "Red"

    # Construct the border to the image

    # Update the GUI pygame
    pygame.display.update()

# Quit the GUI game
pygame.quit()

