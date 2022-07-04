""" The constantes of the program """

import pygame

# Window
TITLE_WINDOW = "Solitaire"
SIZE_WINDOW = (600, 550)
BG_COLOR = (105, 117, 140)
ICON_WINDOW = "imgs/icon.png"


# Pawn
PAWN_IMG = "imgs/pawn.png"
PAWN_SELECT_IMG = "imgs/pawn_select.png"
SIZE_PAWN = (70, 70)


# Grid
INITIALE_GRID = (
    ("1", "1", "p", "p", "p", "1", "1"), # 0 for nothing
    ("1", "p", "p", "p", "p", "p", "1"), # 1 for a border
    ("p", "p", "p", "p", "p", "p", "p"), # p for a pawn
    ("p", "p", "p", "p", "p", "p", "p"), # s for a selected pawn
    ("p", "p", "p", "p", "p", "p", "p"),
    ("1", "p", "p", "p", "p", "p", "1"),
    ("1", "1", "p", "p", "p", "1", "1"),
)
RECT_GRID = pygame.Rect(
    SIZE_WINDOW[0] / 2 - SIZE_PAWN[0] * len(INITIALE_GRID[0]) / 2,
    SIZE_WINDOW[1] / 2 - SIZE_PAWN[1] * len(INITIALE_GRID[1]) / 2,
    SIZE_PAWN[0] * len(INITIALE_GRID[0]),
    SIZE_PAWN[1] * len(INITIALE_GRID[1])
)


# Message and button
BTN_REPLAY_IMG = "imgs/replay.png"
RECT_BTN = pygame.Rect(
    SIZE_WINDOW[0] / 2 - 50,
    SIZE_WINDOW[0] * 0.40,
    100, # Width of the image
    50 # Height of the image
)
