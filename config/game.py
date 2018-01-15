class Game:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Game, cls)

        return cls._instance
