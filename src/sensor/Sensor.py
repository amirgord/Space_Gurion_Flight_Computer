import time
import board
import busio
import adafruit_lsm6ds
from log.Logger import Logger  # Import the Logger class

class Sensor:
    def __init__(self):
        """Initialize I2C bus and sensor."""
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_lsm6ds.LSM6DS33(self.i2c)
        self.logger = Logger("../log/mylog.log")

    def detData(self):
        # Read acceleration and gyro values.
        accel_x, accel_y, accel_z = self.sensor.acceleration
        gyro_x, gyro_y, gyro_z = self.sensor.gyro

        # Write the values to the logger.
        self.logger.write("Acceleration (m/s^2): ({0:.2f}, {1:.2f}, {2:.2f})".format(accel_x, accel_y, accel_z))
        self.logger.write("Gyro (rad/s): ({0:.2f}, {1:.2f}, {2:.2f})".format(gyro_x, gyro_y, gyro_z))





