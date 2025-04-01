import unittest
import pygame
from src.views.start_view import StartView

class TestStartView(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.display = pygame.display.set_mode((800,800))
        
    def tearDown(self):
        pygame.quit()
        
    def test_start_view_creation(self):
        view = StartView(self.display)
        
        self.assertEqual(view.screen, self.display)
        self.assertEqual(view.input_text, "")
        
        
        
    def test_typing_event(self):
        view = StartView(self.display)
        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_b, "unicode":"b"})
        view.handle_event(event)
        
        self.assertEqual(view.input_text, "b")
        
        
        
    def test_backspace_event(self):
        view = StartView(self.display)
        view.input_text = "block"
        event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_BACKSPACE})
        view.handle_event(event)
        
        self.assertEqual(view.input_text, "bloc")