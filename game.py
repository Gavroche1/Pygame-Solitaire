""" This file contains the class which manages the game """

import random
import const

class Game:
    """ This class manages the game """

    def __init__(self):
        """ Initialize """

        self.grid = []
        self.state = "PLAY" # "PLAY" or "WIN" or "LOSE"
        self.select_pawn = None
        self.create_grid()

    def replay(self):
        """ Reset all """

        self.state = "PLAY"
        self.select_pawn = None
        self.create_grid()

    def click_grid(self, posx, posy):
        """ When the user click """

        if self.grid[posy][posx] == "p" and self.select_pawn is None:
            self.grid[posy][posx] = "s" # Select the pawn
            self.select_pawn = (posx, posy)
        elif self.grid[posy][posx] == "p" and self.select_pawn is not None:
            if posy == self.select_pawn[1]: # Horizontal
                if self.select_pawn[0] > posx >= 1 \
                        and self.grid[posy][posx - 1] == "0": # Left
                    self.grid[posy][posx + 1] = "0"
                    self.grid[posy][posx] = "0"
                    self.grid[posy][posx - 1] = "p"
                    self.select_pawn = None
                elif self.select_pawn[0] < posx < len(self.grid[0]) - 1 \
                        and self.grid[posy][posx + 1] == "0": # Right
                    self.grid[posy][posx - 1] = "0"
                    self.grid[posy][posx] = "0"
                    self.grid[posy][posx + 1] = "p"
                    self.select_pawn = None
            elif posx == self.select_pawn[0]: # Vertical
                if self.select_pawn[1] > posy >= 1 \
                        and self.grid[posy - 1][posx] == "0": # Top
                    self.grid[posy + 1][posx] = "0"
                    self.grid[posy][posx] = "0"
                    self.grid[posy - 1][posx] = "p"
                    self.select_pawn = None
                elif self.select_pawn[1] < posy < len(self.grid) - 1 \
                        and self.grid[posy + 1][posx] == "0": # Bottom
                    self.grid[posy - 1][posx] = "0"
                    self.grid[posy][posx] = "0"
                    self.grid[posy + 1][posx] = "p"
                    self.select_pawn = None
        elif self.grid[posy][posx] == "s":
            # Deselect the pawn
            self.grid[posy][posx] = "p"
            self.select_pawn = None


        self.check_state()

    def check_state(self):
        """ Test if the player has win """

        # Count the number of pawns
        nb_pawn = 0
        for row in self.grid:
            for case in row:
                if case in ("p", "s"):
                    nb_pawn += 1

        if nb_pawn == 1:
            self.state = "WIN"
            return

        # Test if the user can remove a pawn
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                # Test if the pawn can move
                if self.grid[i][j] in ("p", "s"):
                    if j > 2 and self.grid[i][j - 2] == "0" \
                            and self.grid[i][j - 1] == "p": # Left
                        self.state = "PLAY"
                        return
                    if j < len(self.grid[0]) - 2 and self.grid[i][j + 2] == "0" \
                            and self.grid[i][j + 1] == "p": # Right
                        self.state = "PLAY"
                        return
                    if i > 2 and self.grid[i - 2][j] == "0" \
                            and self.grid[i - 1][j] == "p": # Top
                        self.state = "PLAY"
                        return
                    if i < len(self.grid) - 2 and self.grid[i + 2][j] == "0" \
                            and self.grid[i+ 1][j] == "p": # Bottom
                        self.state = "PLAY"
                        return

        self.state = "LOSE"

    def create_grid(self):
        """ Create the grid and remove a pawn"""

        # Create the grid
        self.grid = []
        for row in const.INITIALE_GRID:
            self.grid.append(list(row))

        # Remove a pawn
        i = random.randint(0, len(self.grid) - 1)
        j = random.randint(0, len(self.grid[0]) - 1)
        while self.grid[i][j] != "p":
            i = random.randint(0, len(self.grid) - 1)
            j = random.randint(0, len(self.grid[0]) - 1)
        self.grid[i][j] = "0"
