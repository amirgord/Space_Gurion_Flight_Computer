from src.logger.Logger import Logger

class Stabilizer:
    def __init__(self):
        self.logger = Logger()
        self.logger.write("Stabilizer::__init__()")
        pass

    def move(self):
        pass