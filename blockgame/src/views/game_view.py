import pygame
import random

class GameView:
    def __init__(self, screen):
        
        self.screen = screen
        self.display_size = screen.get_size()
        
        self.black_color = (0,0,0)
        self.white_color = (255,255,255)

        self.general_font = pygame.font.Font(None, 30)
        self.input_font = pygame.font.Font(None, 40)
        
        self.init_score_area()
        self.init_grid()
        self.init_block_area()
        self.init_block()
    


        
    

    def init_score_area(self):
        self.score_text = self.general_font.render("SCORE", True, self.white_color)
        
        self.score_center_x = self.display_size[0]
        
        self.score_text_position = (self.score_center_x - 92,20, 100,40)
        self.score_rect = pygame.Rect(self.score_center_x - 100, 50, 90, 40)
        
        self.score_value = 0
        self.text_surface = self.input_font.render(str(self.score_value), True, self.white_color)
        
        self.text_x = self.score_rect.x + (self.score_rect.w - self.text_surface.get_width()) // 2
        self.text_y = self.score_rect.y + (self.score_rect.h - self.text_surface.get_height()) // 2
        

        
    def init_grid(self):
        self.cell_size = 40
        self.grid_size = 9
        self.grid_side_length = self.grid_size * self.cell_size +(self.grid_size-1)
        
        
    def init_block_area(self):
        self.block_frame_rect = pygame.Rect(self.display_size[0] // 2 - (5 * self.cell_size) // 2, self.display_size[1] // 2 + self.grid_side_length // 2 + 5, 5 * self.cell_size, 5 * self.cell_size)
        
    def init_block(self):
        blocks = [
            [(0,0)],
            [(0,0),(1,0),(2,0)],
            [(0,0),(0,1),(1,1)],
            [(0,0),(1,0),(1,1),(1,2)],
            [(0,0),(1,0),(0,1),(1,1),(2,2)]
        ]
        self.current_block = random.choice(blocks)
        self.dragging = False
        self.block_x = self.block_frame_rect.x + self.block_frame_rect.width // 2
        self.block_y = self.block_frame_rect.y + self.block_frame_rect.height // 2
        

        
    
    def draw(self):
        self.screen.fill(self.black_color)
        self.screen.blit(self.score_text, self.score_text_position)

        pygame.draw.rect(self.screen, self.white_color, self.score_rect, 2)
        
    
        self.screen.blit(self.text_surface, (self.text_x, self.text_y))
        
        self.draw_grid()
        
        pygame.draw.rect(self.screen, self.white_color, self.block_frame_rect, 2)
        
        self.draw_block()
        
        
        
    def draw_grid(self):
        for row in range(9):
            for col in range(9):
                x = (self.display_size[0] // 2 - self.grid_side_length // 2) + col *(self.cell_size)
                y = (self.display_size[0] // 2 - self.grid_side_length // 2) + row *(self.cell_size)
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.white_color, rect, 2)
                
    def draw_block(self):  
        for dx, dy in self.current_block:
            x = self.block_x +dx* self.cell_size
            y = self.block_y + dy * self.cell_size
            
            rect = pygame.Rect(x,y, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, self.white_color, rect)
            pygame.draw.rect(self.screen, self.black_color, rect, 2)
        
# osittain generoitu koodi alkaa  
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                for dx, dy in self.current_block:
                    x = self.block_x + dx * self.cell_size
                    y = self.block_y + dy* self.cell_size
                    rect = pygame.Rect(x,y, self.cell_size, self.cell_size)
                    
                    
                    
                    if rect.collidepoint(mouse_pos):
                        self.dragging=True
                        self.drag_offset = (mouse_pos[0] - self.block_x, mouse_pos[1] - self.block_y)
                        break        
# osittain generoitu koodi loppuu

                    
        elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    mouse_pos=event.pos
                    self.block_x = mouse_pos[0] - self.drag_offset[0]
                    self.block_y = mouse_pos[1] - self.drag_offset[1]
                    
        elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.dragging:
                    self.dragging = False
                