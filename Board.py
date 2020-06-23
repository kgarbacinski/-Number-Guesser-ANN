from constants import *
import pygame

class Field:
    def __init__(self, x_start, y_start, is_active=False):
        # Where field starts
        self._x_start = x_start
        self._y_start = y_start
        self._is_active = is_active

        # Field's dimension
        self._f_width = WINDOW_WIDTH // NO_COLS
        self._f_height = WINDOW_HEIGHT // NO_ROWS

    def draw(self, display):
        if self.is_active:
            pygame.draw.rect(display, BLACK, (self._x_start, self._y_start, self._f_width, self._f_height))

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, state):
        self._is_active = state


class Grid:
    def __init__(self):
        self.row_height = 560 // NO_ROWS
        self.col_width = 560 // NO_COLS
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self._fields = []

        # Generate all fields
        self.generate_fields()

    # Creates array with fields for storing some pixels
    def generate_fields(self):
        self._fields = []

        for i in range(NO_ROWS):
            self._fields.append([])
            for j in range(NO_COLS):
                self._fields[i].append(Field(j * self.col_width, i * self.row_height)) # Insert a field into the array,set 0

    # Check which fields've been clicked
    def fnd_clicked_field(self, pos):
        x_pos, y_pos = int(pos[0]), int(pos[1])

        no_col = x_pos // self.col_width # get x-coord of the clicked field
        no_row = y_pos // self.row_height # get y-coord of the clicked field

        return self._fields[no_row][no_col]

    # Draw a whole board
    def draw(self, display):
        for row in self._fields:
            for col in row:
                col.draw(display) # Draw a single field

    # Clear screen when 'R' is pressed
    def cls(self, display):
        display.fill(pygame.Color("White"))
        self.generate_fields()
        pygame.display.update()

    # Shows a prediction
    def show_result(self, val, display):
        display.fill(pygame.Color("White"))

        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surf = my_font.render('Predicted number: ' + str(val), False, BLACK)

        display.blit(text_surf, (WINDOW_WIDTH/2, WINDOW_HEIGHT - 50))
        pygame.display.update()

    def cast_to_binary(self): # Get a grid with only 0|1 values
        binary_matrix = [[] for i in range(NO_ROWS)]

        for no_r in range(len(self._fields)):
            for no_c in range(len(self._fields[no_r])):
                if self._fields[no_r][no_c].is_active:
                    binary_matrix[no_r].append(1)
                else: binary_matrix[no_r].append(0)

        return binary_matrix