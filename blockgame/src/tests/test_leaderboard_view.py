import unittest
import pygame
from src.views.leaderboard_view import LeaderboardView







class TestLeaderboardView(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.display = pygame.display.set_mode((800, 800))
        self.leaderboard = [("Testi1", 20), ("Testi2", 10)]


        def restart_game():
            self.called_restart = True

        def change_player():
            self.called_change_player = True

        self.leaderboard_view = LeaderboardView(self.display, self.leaderboard, restart_game, change_player)
        

    def tearDown(self):
        pygame.quit()

    def test_initialization(self):
        self.assertIsInstance(self.leaderboard_view, LeaderboardView)







    def test_r_event(self):
        view = self.leaderboard_view


        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_r})
        view.handle_event(event)

        self.assertTrue(self.called_restart)



    def test_enter_event(self):
        view = self.leaderboard_view


        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_RETURN})
        view.handle_event(event)

        self.assertTrue(self.called_change_player)




    def test_draw(self):
        view = self.leaderboard_view

        view.draw()


        self.assertEqual(view.ui["colors"]["black_color"], (0, 0, 0))
        self.assertEqual(view.ui["colors"]["white_color"], (255, 255, 255))








