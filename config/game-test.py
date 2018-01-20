import unittest
from unittest.mock import patch
from infra.controller_factory import ControllerFactory
from config.game import Game

class GameTest(unittest.TestCase):
    def test_if_this_class_is_singleton(self):
        instance_one = Game()
        instance_two = Game()
        self.assertEqual(instance_one, instance_two)

    # def test_if_goes_to_home_screen_when_game_starts(self):
    #     with patch.object(ControllerFactory, "dispatch") as mock_dispatch:
    #         game = Game()
    #         game.run()
    #         mock_dispatch.assert_called_with("menu", "home")
