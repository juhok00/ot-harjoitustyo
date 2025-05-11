import pygame

class LeaderboardView:
    """Luokka, joka hoitaa pelin lopputuloksen näyttämisen ja pelaajan vaihtamisen.
    
    Attributes:
        leaderboard: Lista pelaajien nimistä ja pisteistään.
        restart_game: Funktio, joka käynnistää pelin uudelleen.
        change_player: Funktio, joka vaihtaa pelaajan. 
    """


    def __init__(self, screen, leaderboard, restart_game, change_player):
        self.screen = screen
        self.leaderboard = leaderboard
        self.restart_game = restart_game
        self.change_player = change_player

        self.ui = {
            "colors": {
                "black_color": (0,0,0),
                "white_color": (255,255,255),
            },

            "fonts": {
                "title_font": pygame.font.Font(None, 60),
                "general_font": pygame.font.Font(None, 30),
                "input_font": pygame.font.Font(None, 40),
            }
        }

        self.title_text = self.ui["fonts"]["title_font"].render(
            "Game Over", True, self.ui["colors"]["white_color"])

        self.title_position = (self.screen.get_width()//2 - self.title_text.get_width()//2, 50)


    def draw(self):
        """Piirtää pelin lopputuloksen ja pelaajien nimet ja pisteet ruudulle.
        """

        self.screen.fill(self.ui["colors"]["black_color"])
        spacing = 100

### generoitu koodi alkaa


        for i, (player_name, score) in enumerate(self.leaderboard[:10], start=1):
            text = f"{i}. {player_name}: {score}"
            text_surface = self.ui["fonts"]["general_font"].render(
                text, True, self.ui["colors"]["white_color"]
            )
            self.screen.blit(text_surface, (100, spacing))
            spacing += 50

        restart_text = self.ui["fonts"]["general_font"].render(
            "Press R to Retry", True, self.ui["colors"]["white_color"]
        )
        self.screen.blit(
            restart_text,
            (self.screen.get_width() // 2 - restart_text.get_width()
            // 2, self.screen.get_height() - 100),
        )

        change_player_text = self.ui["fonts"]["general_font"].render(
            "Press ENTER to Change Player", True, self.ui["colors"]["white_color"]
        )
        self.screen.blit(
            change_player_text,
            (self.screen.get_width() // 2 - change_player_text.get_width()
            // 2, self.screen.get_height() - 50),
        )

### generoitu koodi loppuu



    def handle_event(self, event):
        """Käsittelee näppäimistön painallukset.
        Args:
            event: Pygame:n tapahtuma.
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.restart_game()
            elif event.key == pygame.K_RETURN:
                self.change_player()
