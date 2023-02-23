import board
import busio
import adafruit_lsm6ds
from src.logger.Logger import Logger

class Sensor:
    def __init__(self):
        """Initialize I2C bus and sensor."""
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_lsm6ds.LSM6DS33(self.i2c)
        self.logger = Logger()
        self.position = (0, 0, 0)
        self.logger.write("Sensor::__init__()")

    def get_data(self):
        # Read acceleration and gyro values.
        self.pos_x, self.pos_y, self.pos_z = self.position
        self.gyro_x, self.gyro_y, self.gyro_z = self.sensor.gyro

        # Write the values to the logger.
        self.logger.write("Position : ({0:.2f}, {1:.2f}, {2:.2f})".format(self.accel_x, self.accel_y, self.accel_z))
        self.logger.write("Gyro (rad/s): ({0:.2f}, {1:.2f}, {2:.2f})".format(self.gyro_x, self.gyro_y, self.gyro_z))

    def check_freefall(self):

        # check direction
        log = self.logger._get_log_filename()
        with open(log, "r") as f:
            lines = f.readlines()
            last_line = lines[-1]
            last_line = last_line.split()
            last_line = last_line[2]
            last_line = last_line.split(",")
            last_line = [float(i) for i in last_line]
            last_line = tuple(last_line)

        # check freefall
        if self.position[2] - last_line[2] > 0.5:
            return True
        else:
            return False
        

    def out_of_curse(self):
        return True

    def ground(self):
        return True



