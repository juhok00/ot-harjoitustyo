import unittest
import pygame
from src.views.game_view import GameView

class TestGameView(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.display = pygame.display.set_mode((800,800))
        self.called = False


    def tearDown(self):        
        pygame.quit()





    def test_game_view_creation(self):
        view = GameView(self.display)

        self.assertEqual(view.screen, self.display)
        self.assertEqual(view.score_value, 0)




    def test_draw(self):
        view = GameView(self.display)

        view.draw()


        self.assertEqual(view.black_color, (0,0,0))
        self.assertEqual(view.white_color, (255,255,255))



    def test_mouse_button_down_dragging_event(self):
        view = GameView(self.display)
        
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {
            "pos": (view.block_x, view.block_y), "button":1})


        view.handle_event(event)

        self.assertTrue(view.dragging)
        self.assertIsNotNone(view.drag_offset)



    def test_that_filling_line_removes_it_and_increases_score(self):
        view = GameView(self.display)

        view.placed_blocks = []

        for col in range(view.grid_size):
            view.placed_blocks.append(([(0,0)], col, 0))

        self.assertEqual(view.score_value, 0)
        view.clear_full_row_or_column()
        self.assertEqual(view.score_value, 1)
        self.assertEqual(len(view.placed_blocks), 0)

    def test_if_no_full_line(self):
        view = GameView(self.display)
        view.clear_full_row_or_column()
        self.assertEqual(view.score_value, 0)

    def test_that_rest_of_the_blocks_stay(self):
        view = GameView(self.display)
        view.placed_blocks = [([(0,0)], 0, 1)]

        for col in range(view.grid_size):
            view.placed_blocks.append(([(0,0)], col, 0))

        view.clear_full_row_or_column()

        self.assertEqual(len(view.placed_blocks), 1)
        self.assertEqual(view.score_value, 1)
