# Import pygame and math modules
import pygame
import math

# Initialize pygame
pygame.init()

# Set the screen size and caption
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Elliptical orbits")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Define some colors in RGB format
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define the center and the radii of the ellipse
center_x = 375
center_y = 300
radius_x = 350
radius_y = 250

# Define the initial angle and angular velocity of the planet
angle = 0
angular_velocity = 0.01

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

    # Draw the sun at the center of the screen
    pygame.draw.circle(screen, blue, (center_x, center_y), 70)

    # Draw the ellipse around the sun
    pygame.draw.ellipse(screen, white, (center_x - radius_x, center_y - radius_y, radius_x * 2, radius_y * 2), 1)

    # Calculate the x and y coordinates of the planet using the parametric equation of the ellipse
    x = center_x + radius_x * math.cos(angle)
    y = center_y + radius_y * math.sin(angle)

    # Draw the planet as a blue circle
    pygame.draw.circle(screen, green, (int(x), int(y)), 50)

    # Update the angle of the planet
    angle += angular_velocity

    # Update the display
    pygame.display.flip()

    # Set the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()