from mako.template import Template

class BoardController:
    def home_action(self):
        template = Template(filename = "views/board.txt")
        print(template.render(line=[0,0,2,2]))

    def back_action(self):
        return "menu"
