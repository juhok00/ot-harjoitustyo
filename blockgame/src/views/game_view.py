import random
import pygame

class GameView:
    """Luokka, joka luo pelinäkymän.
    Mahdollistaa pelin pelaamisen ja pelinäkymän piirtämisen.
    Attributes:
        placed_blocks: Lista sijoitetuista palikoista.
        grid_size: Ruudukon koko.
        grid: Ruudukko, joka sisältää pelin tilan.
        text_surface: Tekstipinta, joka näyttää pistetilanteen.
        dragging: Tieto siitä, onko pelaaja raahaamassa palikkaa.
        block_x: Palikan x-koordinaatti.
        block_y: Palikan y-koordinaatti.
    """


    def __init__(self, screen, display):
        """Konstruktori GameView-luokalle.
        Luo pelinäkymän ja alustaa tarvittavat muuttujat.

        Args:
            screen: Näyttöalue, johon peli piirretään.
        """

        self.screen = screen
        self.display = display
        self.display_size = screen.get_size()

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

        self.player_name = ""
        self.placed_blocks = []
        self.grid_size = 9
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.score_value = 0

        self.text_surface = None
        self.dragging = False
        self.block_x = 0
        self.block_y = 0
        self.drag_offset = None
        self.block_can_fit = False
        self.game_over = False


        self.init_score_area()
        self.init_grid()
        self.init_block_area()
        self.init_block()




    def init_score_area(self):
        """Konstruktori, joka luo alueen pistetilanteelle.
        """

        self.score_text = self.ui["fonts"]["general_font"].render(
            "SCORE", True, self.ui["colors"]["white_color"])


        self.score_center_x = self.display_size[0]

        self.score_text_position = (self.score_center_x - 92,20, 100,40)
        self.score_rect = pygame.Rect(self.score_center_x - 100, 50, 90, 40)

        self.score_value = 0
        self.text_surface = self.ui["fonts"]["input_font"].render(
            str(self.score_value), True, self.ui["colors"]["white_color"])

        self.text_x = self.score_rect.x + (self.score_rect.w - self.text_surface.get_width()) // 2
        self.text_y = self.score_rect.y + (self.score_rect.h - self.text_surface.get_height()) // 2






    def init_grid(self):
        """Konstruktori, joka luo ruudukon pelille.
        """

        self.cell_size = 40
        self.grid_size = 9
        self.grid_side_length = self.grid_size * self.cell_size +(self.grid_size-1)
        self.start_grid_x = self.display_size[0] // 2-self.grid_side_length // 2
        self.start_grid_y = self.start_grid_x


    def init_block_area(self):
        self.block_frame_rect = pygame.Rect(
            self.display_size[0] // 2 - (5 * self.cell_size) // 2,
            self.display_size[1] // 2 + self.grid_side_length // 2 + 5,
            5 * self.cell_size, 5 * self.cell_size
            )

    def init_block(self):
        """Konstruktori, joka luo palikat.
        Luo palikat ja valitsee niistä satunnaisesti yhden.
        """


        blocks = [
            [(0,0)],
            [(0,0),(1,0)],
            [(0,0),(0,1)],
            [(0,0),(1,0),(2,0)],
            [(0,0),(0,1),(0,2)],
            [(0,0),(0,1),(1,1)],
            [(0,0),(1,0),(1,1)],
            [(0,1),(1,0),(1,1)],
            [(0,0),(1,0),(0,1)],
            [(0,0),(0,1),(1,1),(1,0)],
            [(0,0),(1,0),(1,1),(1,2)],
            [(0,0),(1,0),(0,1),(0,2)],
            [(0,0),(0,1),(0,2),(1,2)],
            [(0,2),(1,0),(1,1),(1,2)],

        ]
        self.current_block = random.choice(blocks)




        block_width = max(dx for dx, dy in self.current_block) + 1
        block_height = max(dy for dx, dy in self.current_block) + 1

        self.block_x = self.block_frame_rect.x + (
            self.block_frame_rect.width - block_width * self.cell_size) // 2

        self.block_y = self.block_frame_rect.y + (
            self.block_frame_rect.height - block_height * self.cell_size) // 2

        self.start_block_x = self.block_x
        self.start_block_y = self.block_y

        if self.placed_blocks and not self.check_if_block_can_fit():
            self.game_over = True
            self.display.switch_leaderboard_view()

    def clear_full_row_or_column(self):
        """Tyhjentää rivin tai sarakkeen, joka on täynnä.
        Tarkistaa, jos rivi tai sarake on täynnä ja tyhjentää sen, samalla lisäten pisteet
        """


        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]


        for block_shape, block_x, block_y in self.placed_blocks:
            for dx, dy in block_shape:
                self.grid[block_y + dy][block_x + dx] = 1

        full_row = [
            row_x for row_x in range(self.grid_size) if all(self.grid[row_x][col_x] == 1
            for col_x in range(self.grid_size))
        ]

        full_col = [
            col_x for col_x in range(self.grid_size) if all(self.grid[row_x][col_x] == 1
            for row_x in range(self.grid_size))
        ]

        if not full_row and not full_col:
            return

        cleared_rows_or_columns = len(full_row)+len(full_col)
        self.score_value += cleared_rows_or_columns

        self.text_surface = self.ui["fonts"]["input_font"].render(
            str(self.score_value), True, self.ui["colors"]["white_color"])

### generoitu koodi

        new_placed_blocks = []

        for block_shape, block_x, block_y in self.placed_blocks:
            new_shape = []
            for dx, dy in block_shape:
                gx = block_x + dx
                gy = block_y + dy
                if gy not in full_row and gx not in full_col:
                    new_shape.append((dx,dy))
            if new_shape:
                new_placed_blocks.append((new_shape, block_x, block_y))

        self.placed_blocks = new_placed_blocks

### generoitu koodi loppuu


    def check_if_block_can_fit(self):
        """Tarkistaa, mahtuuko palikka ruudukkoon.
        Tarkistaa, onko palikka mahdollista sijoittaa ruudukkoon.
        """

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                valid = True
                for dx, dy in self.current_block:
                    cx = col + dx
                    cy = row + dy
                    if cx < 0 or cx >= self.grid_size or cy < 0 or cy >= self.grid_size:
                        valid = False
                        break
                    if self.grid[cy][cx] == 1:
                        valid = False
                        break
                if valid:
                    return True
        return False




    def draw(self):
        """Piirtää pelinäkymän.
        Piirtää ruudukon, palikat ja pistetilanteen.
        """


        self.screen.fill(self.ui["colors"]["black_color"])
        self.screen.blit(self.score_text, self.score_text_position)

        pygame.draw.rect(self.screen, self.ui["colors"]["white_color"], self.score_rect, 2)


        self.screen.blit(self.text_surface, (self.text_x, self.text_y))

        if self.game_over:
            font = self.ui["fonts"]["general_font"].render(
                "GAME OVER", True, self.ui["colors"]["white_color"])


            font_rect = font.get_rect(center=(self.display_size[0] // 2, self.display_size[1] // 2))
            self.screen.blit(font, font_rect)
            return

        self.draw_grid()
        self.draw_placed_blocks()

        pygame.draw.rect(self.screen, self.ui["colors"]["white_color"], self.block_frame_rect, 2)

        self.draw_block()





    def draw_grid(self):
        """Piirtää pelialustana toimivan ruudukon.
        """


        for row in range(9):
            for col in range(9):
                x = (self.display_size[0] // 2 - self.grid_side_length // 2) + col *(self.cell_size)
                y = (self.display_size[0] // 2 - self.grid_side_length // 2) + row *(self.cell_size)
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.ui["colors"]["white_color"], rect, 2)

    def draw_block(self):
        """Piirtää palikan.
        """


        for dx, dy in self.current_block:
            x = self.block_x +dx* self.cell_size
            y = self.block_y + dy * self.cell_size

            rect = pygame.Rect(x,y, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, self.ui["colors"]["white_color"], rect)
            pygame.draw.rect(self.screen, self.ui["colors"]["white_color"], rect, 2)



    def draw_placed_blocks(self):
        """Piirtää sijoitetut palikat.
        """

        for block in self.placed_blocks:
            block_shape, block_x, block_y = block
            for dx, dy in block_shape:
                x = self.start_grid_x + (block_x + dx) * self.cell_size
                y = self.start_grid_y + (block_y + dy) * self.cell_size
                rect = pygame.Rect(x,y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.ui["colors"]["white_color"], rect)
                pygame.draw.rect(self.screen, self.ui["colors"]["white_color"], rect, 2)


### osittain generoitu koodi alkaa
    def handle_event(self, event):
        """Käsittelee pelinäkymän tapahtumat.
        Mahdollistaa hiiren painallukset ja liikkeet, jonka avulla pelaaja voi raahata palikkoja.

        Args:
            event: Objekti, joka käsittää tiedon hiiren toiminnasta.
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                for dx, dy in self.current_block:
                    x = self.block_x + dx * self.cell_size
                    y = self.block_y + dy* self.cell_size
                    rect = pygame.Rect(x,y, self.cell_size, self.cell_size)

                    if rect.collidepoint(mouse_pos):
                        self.dragging=True
                        self.drag_offset= (mouse_pos[0] - self.block_x, mouse_pos[1] - self.block_y)
                        break
### osittain generoitu koodi loppuu

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_pos=event.pos
                self.block_x = mouse_pos[0] - self.drag_offset[0]
                self.block_y = mouse_pos[1] - self.drag_offset[1]




        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.dragging:
                self.dragging = False

                lock_x = (self.block_x - self.start_grid_x + self.cell_size // 2) // self.cell_size
                lock_y = (self.block_y - self.start_grid_y + self.cell_size // 2) // self.cell_size



### Generoitu koodi alkaa
                valid = True
                for dx, dy in self.current_block:
                    cx = lock_x + dx
                    cy = lock_y + dy
                    if cx < 0 or cx >= self.grid_size or cy < 0 or cy >= self.grid_size:
                        valid = False
                        break

                if valid:
                    for block in self.placed_blocks:
                        existing_shape, existing_x, existing_y = block
                        for edx, edy in existing_shape:
                            for dx, dy in self.current_block:
                                if (existing_x + edx == lock_x + dx and
                                    existing_y + edy == lock_y + dy):
                                    valid = False
                                    break
                            if not valid:
                                break
                        if not valid:
                            break
### Generoitu koodi loppuu

                if valid:
                    self.placed_blocks.append((self.current_block.copy(), lock_x, lock_y))

                    self.clear_full_row_or_column()

                    self.init_block()
                else:
                    self.block_x = self.start_block_x
                    self.block_y = self.start_block_y
