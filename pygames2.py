# Import pygame and sys modules
import pygame
import sys

# Initialize pygame
pygame.init()

# Set the screen size and caption
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing ball")

# Define some colors in RGB format
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0,0, 255)

# Define the initial position and radius of the ball
x = 375
y = 375
radius = 70

# Define the initial speed and direction of the ball
speed_x = 0.2
speed_y = 0.2
direction_x = 1
direction_y = 1

# Define a loop variable to keep the simulation running
running = True

# Start the main loop
while running:
    # Handle the events in the event queue
    for event in pygame.event.get():
        # If the user clicks the close button, exit the loop
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black color
    screen.fill(black)

    # Update the position of the ball
    x += speed_x * direction_x
    y += speed_y * direction_y

    # Check if the ball hits the edges of the screen and reverse the direction
    if x - radius < 0 or x + radius > 800:
        direction_x = -direction_x
    if y - radius < 0 or y + radius > 600:
        direction_y = -direction_y

    # Draw the ball as a red circle
    pygame.draw.circle(screen, blue, (x, y), radius)

    # Update the display
    pygame.display.flip()
pygame.quit()