from Car import Cars
from Bus import Buses
from Truck import Trucks

def in_data(line):
    cd = Cars()
    if line[0] == 0:
        cd = Trucks()
    elif line[0] == 1:
        cd = Buses()
    cd.In(line)
    return cd