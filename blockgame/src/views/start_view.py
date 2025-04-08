import pygame


class StartView:
    def __init__(self, screen, game_view):
        
        self.screen = screen
        self.display_size = screen.get_size()
        self.game_view = game_view
        

        self.background_color = (0,0,0)
        self.text_color = (255,255,255)
        self.button_color = (255,255,255)

        self.title_font = pygame.font.Font(None, 60)
        self.general_font = pygame.font.Font(None, 30)


        self.title_text = self.title_font.render("BLOCKDROP", True, self.text_color)
        self.title_position = (self.display_size[0]//2 - self.title_text.get_width()//2, 300)
        
        
        self.name_text = self.general_font.render("ENTER NAME", True, self.text_color)
        self.name_position = (self.display_size[0]//2 - self.name_text.get_width()//2, 400)

        self.input_text = ""
        self.input_font = pygame.font.Font(None, 40)
        self.input_rect = pygame.Rect(self.display_size[0] // 2 - 100, 450, 200, 40)



    def draw(self):
        self.screen.fill(self.background_color)
        self.screen.blit(self.title_text, self.title_position)
        self.screen.blit(self.name_text, self.name_position)


        pygame.draw.rect(self.screen, self.text_color, self.input_rect, 2)
        text_surface = self.input_font.render(self.input_text, True, self.text_color)
        
        text_x = self.input_rect.x + (self.input_rect.w - text_surface.get_width()) // 2
        text_y = self.input_rect.y + (self.input_rect.h - text_surface.get_height()) // 2

        self.screen.blit(text_surface, (text_x, text_y))
        


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.key == pygame.K_RETURN:
                if self.input_text.strip():
                    self.game_view(self.input_text)
                
                
                
            elif len(self.input_text) < 10:
                self.input_text += event.unicode
                
                
