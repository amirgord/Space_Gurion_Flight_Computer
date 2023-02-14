from src.logger.Logger import Logger

class Parachute:
    def __init__(self):
        self.logger = Logger()
        self.logger.write("Parachute::__init__()")
        pass

    def open(self):
        pass