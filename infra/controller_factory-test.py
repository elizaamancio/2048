import unittest
from unittest.mock import MagicMock
from infra.controller_factory import ControllerFactory
from config.key_mapping import key_mapping

class ControllerFactoryTest(unittest.TestCase):
    def test_if_calls_equivalent_key_value_when_x_command_is_sent(self):
        controller_factory = ControllerFactory()
        screen = "menu"
        command = "x"
        key = "menu_x"
        key_mapping[key] = MagicMock()
        controller_factory.dispatch(screen, command)
        key_mapping[key].assert_called_with()

    def test_if_calls_equivalent_key_value_when_s_command_is_sent(self):
        controller_factory = ControllerFactory()
        screen = "menu"
        command = "s"
        key = "menu_s"
        key_mapping[key] = MagicMock()
        controller_factory.dispatch(screen, command)
        key_mapping[key].assert_called_with()
