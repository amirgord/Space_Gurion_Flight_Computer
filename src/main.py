from log.Logger import Logger
from src.sensor.Sensor import Sensor

# import "bit/"
# import "parachute/Parachute.py"
# import "radio/Radio.py"
# import "../log/Logger.py"

def main():
    #Initilize sesors & write to looger: -------------
    # Parachute parachute
    sensor = Sensor();
    # Radio radio
    logger = Logger();
    
    
    #BIT & write to looger: ----------
    
    
    #Main loop:
    while True:
        #get data from sensors.
        #  the sensor write to looger
        sensor.getData();

        #open parachute & write to looger: ------------


        #send data & write to looger: --------
        break
        

if __name__ == '__main__':
    main()