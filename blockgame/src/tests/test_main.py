import unittest
import pygame
from src.main import Display

class TestMain(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.display = Display(800, 800, "BlockGame")

    def tearDown(self):
        pygame.quit()



    def test_display_creation(self):
        self.assertIsNotNone(self.display.screen)
        self.assertIsNotNone(self.display.start_view)
        self.assertIsNotNone(self.display.game_view)
        self.assertIsNotNone(self.display.leaderboard_view)
        self.assertEqual(self.display.current_view, self.display.start_view)


    def test_switch_start_view(self):
        self.display.switch_start_view()
        self.assertEqual(self.display.current_view, self.display.start_view)
        self.assertEqual(self.display.start_view.input_text, "")
        self.assertFalse(self.display.game_view.game_over)


    def test_switch_game_view(self):
        self.display.switch_game_view("Testi1")
        self.assertEqual(self.display.current_view, self.display.game_view)
        self.assertEqual(self.display.game_view.player_name, "Testi1")


    def test_switch_leaderboard_view(self):
        self.display.switch_game_view("Testi1")
        self.display.switch_leaderboard_view()
        self.assertEqual(self.display.current_view, self.display.leaderboard_view)
        self.assertEqual(self.display.leaderboard[0], ("Testi1", 0))


    def test_restart_game(self):
        self.display.game_view.player_name = "Testi1"
        self.display.restart_game()
        self.assertEqual(self.display.current_view, self.display.game_view)
        self.assertEqual(self.display.game_view.player_name, "Testi1")
        self.assertFalse(self.display.game_view.game_over)


