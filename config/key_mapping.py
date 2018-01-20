from controllers.menu_controller import MenuController
from controllers.board_controller import BoardController

menu_controller = MenuController()
board_controller = BoardController()

key_mapping = {
    "menu_x": menu_controller.exit_action,
    "menu_s": menu_controller.start_action,
    "menu_home": menu_controller.home_action,
    "board_home": board_controller.home_action,
    "board_b": board_controller.back_action
}
