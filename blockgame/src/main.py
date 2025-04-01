import pygame
from views.start_view import StartView


class Display:
    def __init__(self, width, height, title):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption(title)
        self.start_view = StartView(self.screen)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                self.start_view.handle_event(event)


            self.start_view.draw()
            pygame.display.flip()

        pygame.quit()





def main():
    game = Display(800,800, "BlockGame")

    game.run()


if __name__=="__main__":
    main()