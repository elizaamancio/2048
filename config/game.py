from infra.controller_factory import ControllerFactory
import readchar
import os

class Game:
    DEFAULT_COMMAND = "home"
    _instance = None
    screen = "menu"
    command = "home"

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(Game)

        return cls._instance

    def run(cls):
        controller_factory = ControllerFactory()
        error_message = None


        while True:
            try:
                os.system("clear")
                screen_redirect = controller_factory.dispatch(cls.screen, cls.command)

                if screen_redirect:
                    cls.screen = screen_redirect
                    cls.command = cls.DEFAULT_COMMAND
                    continue

                if error_message:
                    print(error_message)

                cls.command = readchar.readchar()
                error_message = None
            except Exception as error:
                print(str(error))
                error_message = "Invalid Comand!"
                cls.command = cls.DEFAULT_COMMAND
