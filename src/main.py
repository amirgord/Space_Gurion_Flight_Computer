from src.logger.Logger import Logger
from src.parachute.Parachute import Parachute
from src.radio.Radio import Radio
from src.sensor.Sensor import Sensor


def main():
    #Initilize:
    parachute = Parachute();
    sensor = Sensor();
    radio = Radio();
    logger = Logger();
    
    #BIT:

    #Main loop:
    while True:
        #get data from sensors:
        sensor.getData();

        #check open parachute:

        #check move:

        #send data:
        break
        

if __name__ == '__main__':
    main()