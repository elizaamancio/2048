class Field:
    def __init__(self, value):
        self.value = value
        self.squeezed = False

    def squeeze(self):
        self.value *= 2
        self.squeezed = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__



