import unittest
from config.game import Game

class GameTest(unittest.TestCase):
    def test_if_this_class_is_singleton(self):
        instance_one = Game()
        instance_two = Game()
        self.assertEqual(instance_one, instance_two)
