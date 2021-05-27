from Car import Cars
from Bus import Buses
from LightCar import LightCar
from Truck import Trucks


def in_data(line):
    cd = Cars()
    if line[0] == 0:
        cd = Trucks()
    elif line[0] == 1:
        cd = Buses()
    elif line[0] == 2:
        cd = LightCar()

    cd.in_information(line)

    return cd
