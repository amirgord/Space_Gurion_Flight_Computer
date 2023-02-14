from log.Logger import Logger

class Radio:
    def __init__(self):
        self.logger = Logger()
        self.logger.write("Radio::__init__()")
        pass

    def send(self, info):
        pass