import pygame
from views.start_view import StartView
from views.game_view import GameView


class Display:
    def __init__(self, width, height, title):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption(title)
        
        self.start_view = StartView(self.screen, self.switch_game_view)
        self.game_view = GameView(self.screen)
        
        self.current_view = self.start_view
        

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                self.current_view.handle_event(event)


            self.current_view.draw()
            pygame.display.flip()

        pygame.quit()
        
    def switch_game_view(self, player_name):
        self.game_view.player_name = player_name
        self.current_view = self.game_view





def main():
    game = Display(800,800, "BlockGame")

    game.run()


if __name__=="__main__":
    main()