import pygame
from constants import *
from Board import Field, Grid
from Guesser import *


def init_display():
    pygame.init()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Number Predictor")
    display.fill(pygame.Color("White"))
    pygame.display.update()

    grid = Grid()
    return display, grid


def main():
    display, grid = init_display()
    guesser = Guesser() # used when we guess a number

    is_run = True
    while is_run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # When user press any button
                if event.key == pygame.K_r:
                    grid.cls(display)
                else:
                    mnist = grid.cast_to_binary()
                    num = guesser.predict_num(mnist)
                    grid.show_result(num, display)

            if pygame.mouse.get_pressed()[0]: # Left mouse button down
                mouse_pos = pygame.mouse.get_pos()

                clicked_field = grid.fnd_clicked_field(mouse_pos)
                clicked_field.is_active = True # Set field as active

            elif event.type == pygame.QUIT:
                is_run = False

        grid.draw(display)
        pygame.display.update()


if __name__ == "__main__":
    main()