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
