from src.bit.BIT import BIT
from src.logger.Logger import Logger
from src.parachute.Parachute import Parachute
from src.radio.Radio import Radio
from src.sensor.Sensor import Sensor
from src.stabilize.Stabilizer import Stabilizer


def main():
    logger = Logger()

    logger.write("---------------------- Initilize ----------------------")
    parachute = Parachute()
    sensor = Sensor()
    radio = Radio()
    stabilizer = Stabilizer()
    bit = BIT()


    logger.write("---------------------- BIT ----------------------")
    bit.test()


    logger.write("---------------------- Main loop ----------------------")
    while True:
        #get data from sensors:
        data = sensor.get_data()

        #check open parachute:
        if sensor.check_freefall():
            parachute.open()

        #check move:
        if sensor.out_of_curse():
            stabilizer.move()

        #send data:
        radio.send(data)

        #check if ground:
        if sensor.ground():
            break


if __name__ == '__main__':
    main()