import unittest
import pygame
from src.views.start_view import StartView


class TestStartView(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.display = pygame.display.set_mode((800,800))
        self.called = False




    def tearDown(self):
        pygame.quit()


    def game_view_test(self, player_name = None):
        self.called = True

    def test_start_view_creation(self):
        view = StartView(self.display, self.game_view_test)

        self.assertEqual(view.screen, self.display)
        self.assertEqual(view.input_text, "")


    def test_typing_event(self):
        view = StartView(self.display, self.game_view_test)
        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_b, "unicode":"b"})
        view.handle_event(event)

        self.assertEqual(view.input_text, "b")



    def test_backspace_event(self):
        view = StartView(self.display, self.game_view_test)
        view.input_text = "block"
        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_BACKSPACE})
        view.handle_event(event)

        self.assertEqual(view.input_text, "bloc")


    def test_enter_event(self):
        view = StartView(self.display, self.game_view_test)

        view.input_text = "test"

        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_RETURN})
        view.handle_event(event)

        self.assertTrue(self.called)


    def test_draw(self):
        view = StartView(self.display, self.game_view_test)

        view.draw()


        self.assertEqual(view.ui["colors"]["background_color"], (0,0,0))
        self.assertEqual(view.ui["colors"]["text_color"], (255,255,255))
        self.assertEqual(view.ui["colors"]["button_color"],(255,255,255))
