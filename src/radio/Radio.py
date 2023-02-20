import time
import threading
import spidev
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24

from src.logger.Logger import Logger

class Radio(threading.Thread):
    def __init__(self):
        self.logger = Logger()

        
        self.configureGPIO()

        # Create an instance of the nRF24L01 module
        self.radio = NRF24(GPIO, spidev.SpiDev())
        self.radio.begin(0, 25)

        # Define the data packet format
        self.data_packet = [0] * 32

        self.logger.write("Radio::__init__()")
        pass


    def configureGPIO(self):

        # Configure the GPIO pins for the radio module
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.IN)


    # Set the frequency and channel for the radio module
    def setFrequency(self, frequency):

        self.radio.setChannel(0x76)
        self.radio.setDataRate(NRF24.BR_1MBPS)
        self.radio.setPALevel(NRF24.PA_MAX)

        # Set the addresses for the self.radio module (both sender and receiver must have the same addresses)
        pipe = [0xE7, 0xE7, 0xE7, 0xE7, 0xE7]
        self.radio.openWritingPipe(pipe)
        self.radio.openReadingPipe(1, pipe)






    def send(self,data):

        while len(data) > 0:
            for i in range(0, 32):
                if len(data) > 0:
                    self.data_packet[i] = ord(data[0])
                    data = data[1:]
                else:
                    break

        # Write data to the radio module
        self.radio.write(self.data_packet)

        # Process the received data packet
        self.logger.write("send data:", self.data_packet)

