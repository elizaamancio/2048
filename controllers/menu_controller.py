from mako.template import Template
import readchar
import sys

class MenuController:
    def exit_action(self):
        print("Do you really wanna leave? (Y|N)")
        confirmation = readchar.readchar()

        if confirmation.upper() == "Y":
            sys.exit()

    def start_action(self):
        return "board"

    def home_action(self):
        template = Template(filename = "views/home.txt")
        print(template.render())
