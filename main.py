""" A simple game """

import pygame
import game
import event as event_file
import const

class Window:
    """ This class is the window of the program """

    def __init__(self):
        """ Initialize """

        pygame.init()
        pygame.display.set_caption(const.TITLE_WINDOW)
        pygame.display.set_icon(pygame.image.load(const.ICON_WINDOW))

        self.screen = pygame.display.set_mode(const.SIZE_WINDOW)
        self.finished = False
        self.images = {
            "pawn": pygame.image.load(const.PAWN_IMG).convert_alpha(),
            "pawn_select": pygame.image.load(const.PAWN_SELECT_IMG).convert_alpha(),
            "btn_replay": pygame.image.load(const.BTN_REPLAY_IMG).convert_alpha(),
        }
        self.fonts = {
            "message": pygame.font.SysFont("Arial", 45),
        }
        self.game = game.Game()
        self.mainloop()

    def mainloop(self):
        """ In this function there is the main loop of the program """

        clock = pygame.time.Clock()
        event = event_file.Event()
        event.add_event(pygame.QUIT, self.quit)
        event.add_event(pygame.MOUSEBUTTONDOWN, self.click)

        while not self.finished:
            clock.tick(60)
            self.draw_screen()
            event.execute()

        pygame.quit()

    def draw_screen(self):
        """ Display all on the screen """

        # The background
        pygame.draw.rect(
            self.screen,
            const.BG_COLOR,
            pygame.Rect(0, 0, const.SIZE_WINDOW[0], const.SIZE_WINDOW[1])
        )

        # The grid with the pawns
        for i in range(len(self.game.grid)):
            for j in range(len(self.game.grid[i])):
                # The grid pattern
                if const.INITIALE_GRID[i][j] == "p":
                    if j % 2 - i % 2 == 0:
                        color_rect = (217, 215, 204)
                    else:
                        color_rect = (148, 155, 166)

                    pygame.draw.rect(
                        self.screen,
                        color_rect,
                        pygame.Rect(
                            j * const.SIZE_PAWN[0] + const.RECT_GRID.x,
                            i * const.SIZE_PAWN[1] + const.RECT_GRID.y,
                            const.SIZE_PAWN[0],
                            const.SIZE_PAWN[1]
                        )
                    )

                # The pawns
                if self.game.grid[i][j] == "p":
                    self.screen.blit(
                        self.images["pawn"],
                        (
                            j * const.SIZE_PAWN[0] + const.RECT_GRID.x,
                            i * const.SIZE_PAWN[1] + const.RECT_GRID.y
                        )
                    )
                elif self.game.grid[i][j] == "s":
                    self.screen.blit(
                        self.images["pawn_select"],
                        (
                            j * const.SIZE_PAWN[0] + const.RECT_GRID.x,
                            i * const.SIZE_PAWN[1] + const.RECT_GRID.y
                        )
                    )

        if self.game.state == "LOSE":
            self.display_message("You lose !")
        elif self.game.state == "WIN":
            self.display_message("You win !!")

        pygame.display.flip()

    def display_message(self, message):
        """ Show a rectangle with a message and a button to replay """

        pygame.draw.rect(
            self.screen,
            (217, 215, 204),
            pygame.Rect(
                const.SIZE_WINDOW[0] * 0.05,
                const.SIZE_WINDOW[0] * 0.10,
                const.SIZE_WINDOW[0] * 0.90,
                const.SIZE_WINDOW[1] * 0.50
            )
        )

        text = self.fonts["message"].render(message, True, (0, 0, 0))
        text_rect = text.get_rect(
            center=(
                const.SIZE_WINDOW[0] / 2,
                const.SIZE_WINDOW[0] * 0.30
            )
        )
        self.screen.blit(text, text_rect)

        self.screen.blit(self.images["btn_replay"], const.RECT_BTN)


    def click(self, evt):
        """ When the user clicks on the window """

        posx, posy = evt.pos[0], evt.pos[1]

        if const.RECT_GRID.collidepoint(posx, posy) \
                and self.game.state == "PLAY": # The grid
            self.game.click_grid(
                int((posx - const.RECT_GRID.x) // const.SIZE_PAWN[0]),
                int((posy - const.RECT_GRID.y) // const.SIZE_PAWN[1])
            )
        elif const.RECT_BTN.collidepoint(posx, posy): # Replay btn
            self.game.replay()

    def quit(self, evt):
        """ Close the window and quit the program """

        self.finished = True

def main():
    """ The main function which launch the window """

    Window()

if __name__ == "__main__":
    main()
