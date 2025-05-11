import unittest
import pygame
from src.views.game_view import GameView

class TestGameView(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.display = pygame.display.set_mode((800,800))
        self.game_display = pygame.Surface((800, 800))
        self.view = GameView(self.display, self.game_display)



    def tearDown(self):        
        pygame.quit()





    def test_game_view_creation(self):
        view = GameView(self.display, self.game_display)

        self.assertEqual(view.screen, self.display)
        self.assertEqual(view.score_value, 0)




    def test_draw(self):
        view = GameView(self.display, self.game_display)

        view.draw()

        self.assertEqual(view.ui["colors"]["black_color"], (0, 0, 0))
        self.assertEqual(view.ui["colors"]["white_color"], (255, 255, 255))




    def test_that_filling_line_removes_it_and_increases_score(self):
        view = GameView(self.display, self.game_display)

        view.placed_blocks = []

        for col in range(view.grid_size):
            view.placed_blocks.append(([(0,0)], col, 0))

        self.assertEqual(view.score_value, 0)
        view.clear_full_row_or_column()
        self.assertEqual(view.score_value, 1)
        self.assertEqual(len(view.placed_blocks), 0)

    def test_if_no_full_line(self):
        view = GameView(self.display, self.game_display)
        view.clear_full_row_or_column()
        self.assertEqual(view.score_value, 0)

    def test_that_rest_of_the_blocks_stay(self):
        view = GameView(self.display, self.game_display)
        view.placed_blocks = [([(0,0)], 0, 1)]

        for col in range(view.grid_size):
            view.placed_blocks.append(([(0,0)], col, 0))

        view.clear_full_row_or_column()

        self.assertEqual(len(view.placed_blocks), 1)
        self.assertEqual(view.score_value, 1)


    def test_mouse_motion(self):
        view = GameView(self.display, self.game_display)
        view.init_block()

        event_button_down = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (view.block_x, view.block_y), "button": 1})

        view.handle_event(event_button_down)


        event_mouse_motion = pygame.event.Event(pygame.MOUSEMOTION, {"pos": (view.block_x+10, view.block_y+10)})

        view.handle_event(event_mouse_motion)

        self.assertEqual(view.block_x, view.start_block_x + 10)
        self.assertEqual(view.block_y, view.start_block_y + 10)


    def test_mouse_up_event(self):
        view = GameView(self.display, self.game_display)
        view.init_block()


        event_button_down = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (view.block_x, view.block_y), "button": 1})
        view.handle_event(event_button_down)

        event_mouse_motion = pygame.event.Event(pygame.MOUSEMOTION, {"pos": (view.start_grid_x+5, view.start_grid_y+5)})
        view.handle_event(event_mouse_motion)


        event_button_up = pygame.event.Event(pygame.MOUSEBUTTONUP, {"button": 1})
        view.handle_event(event_button_up)


        self.assertFalse(view.dragging)


            
        grid_has_block = any(1 in row for row in view.grid)
        self.assertTrue(grid_has_block)


