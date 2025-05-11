import pygame
from src.views.start_view import StartView
from src.views.game_view import GameView
from src.views.leaderboard_view import LeaderboardView


class Display:
    """Main luokka, joka hoitaa pelin pyörityksen ja näkymien vaihdot.
    """

    def __init__(self, width, height, title):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption(title)
        self.leaderboard = []

        self.start_view = StartView(self.screen, self.switch_game_view)
        self.game_view = GameView(self.screen, self)

        self.leaderboard_view = LeaderboardView(
            self.screen, self.leaderboard, self.restart_game, self.switch_start_view)


        self.current_view = self.start_view


    def run(self):
        """Pelin pääsilmukka, joka hoitaa tapahtumien käsittelyn ja näkymien piirtämisen.
        """

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                self.current_view.handle_event(event)

            self.current_view.draw()
            pygame.display.flip()

        pygame.quit()

    def switch_start_view(self):
        """Vaihtaa näkymän aloitusnäkymään.
        """

        self.start_view.input_text = ""
        self.game_view.game_over = False
        self.current_view = self.start_view

    def switch_game_view(self, player_name):
        """Vaihtaa näkymän pelinäkymään.
        Args:
            player_name: Pelaajan nimi, joka syötetään aloitusnäkymässä.
        """


        self.game_view = GameView(self.screen, self)
        self.game_view.player_name = player_name
        self.current_view = self.game_view

    def switch_leaderboard_view(self):
        """Vaihtaa näkymän leaderboard-näkymään.
        """

        self.leaderboard.append((self.game_view.player_name, self.game_view.score_value))
        self.leaderboard.sort(key=lambda x: x[1], reverse=True)

        self.current_view = self.leaderboard_view


    def restart_game(self):
        """Uudelleenkäynnistää pelin ja palauttaa näkymän pelinäkymään.
        """

        player_name = self.game_view.player_name
        self.game_view = GameView(self.screen, self)
        self.game_view.player_name = player_name
        self.game_view.game_over = False
        self.current_view = self.game_view





def main():
    game = Display(800,800, "BlockGame")

    game.run()


if __name__=="__main__":
    main()
