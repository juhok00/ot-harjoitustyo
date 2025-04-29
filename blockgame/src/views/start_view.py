import pygame


class StartView:
    """Luokka, joka luo aloitusnäkymän.
    Mahdollistaa pelaajan nimen syöttämisen ja pelinäkymään siirtymisen.
    Attributes:
        game_view:  Funktio, jolla pelaaja siirtyy pelinäkymään nimen syöttämisen jälkeen.
        ui: Sanakirja, johon sisältyy käyttöliittymän värit ja fontit.
    """

    def __init__(self, screen, game_view):
        """StartView luokan konstruktori.

        Args:
            game_view: Funktio, jolla pelaaja siirtyy pelinäkymään nimen syöttämisen jälkeen.
        """

        self.screen = screen
        self.display_size = screen.get_size()
        self.game_view = game_view

        self.ui = {
            "colors": {
                "background_color": (0,0,0),
                "text_color": (255,255,255),
                "button_color": (255,255,255),
            },

            "fonts": {
                "title_font": pygame.font.Font(None, 60),
                "general_font": pygame.font.Font(None, 30),
                "input_font": pygame.font.Font(None, 40),
            }

        }

        self.title_text = self.ui["fonts"]["title_font"].render(
            "BLOCKDROP", True, self.ui["colors"]["text_color"]
        )
        self.title_position = (self.display_size[0]//2 - self.title_text.get_width()//2, 300)



        self.name_text = self.ui["fonts"]["general_font"].render(
            "ENTER NAME", True, self.ui["colors"]["text_color"]
        )
        self.name_position = (self.display_size[0]//2 - self.name_text.get_width()//2, 400)



        self.input_text = ""
        self.input_rect = pygame.Rect(self.display_size[0] // 2 - 100, 450, 200, 40)



    def draw(self):
        """Piirtää näytön aloitusnäkymän.
        """

        self.screen.fill(self.ui["colors"]["background_color"])
        self.screen.blit(self.title_text, self.title_position)
        self.screen.blit(self.name_text, self.name_position)


        pygame.draw.rect(self.screen, self.ui["colors"]["text_color"], self.input_rect, 2)
        text_surface = self.ui["fonts"]["input_font"].render(
            self.input_text, True, self.ui["colors"]["text_color"]
        )

        text_x = self.input_rect.x + (self.input_rect.w - text_surface.get_width()) // 2
        text_y = self.input_rect.y + (self.input_rect.h - text_surface.get_height()) // 2

        self.screen.blit(text_surface, (text_x, text_y))



    def handle_event(self, event):
        """Käsittelee aloitussivun tapahtumat, kuten näppäimistön painallukset.
        Mahdollistaa nimen kirjoittamisen ja siitä etenemisen pelinäkymään.

        Args:
            event: Objekti, joka käsittää tiedon näppäimen painamisesta.
        """


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.key == pygame.K_RETURN:
                if self.input_text.strip():
                    self.game_view(self.input_text)


            elif len(self.input_text) < 10:
                self.input_text += event.unicode
