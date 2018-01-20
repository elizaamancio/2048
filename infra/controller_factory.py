from config.key_mapping import key_mapping

class ControllerFactory:
    def dispatch(self, screen, command):
        key = "{}_{}".format(screen, command)
        action = key_mapping[key]
        return action()
