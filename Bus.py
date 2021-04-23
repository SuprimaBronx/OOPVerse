from Car import Cars


class Buses(Cars):

    def __init__(self):
        super().__init__()
        self.type = 'Bus'
        self.passenger = 0

    def In(self, line):
        self.passenger = line[1]
        self.engine_power = line[2]
        self.global_weight = line[1] * 75
        self.ratio_calc()


    def display(self, file, i):
        file.write(str(i) +'.Автобус' + "\n")
        file.write('Пассажировместимость: ' + str( self.passenger) + "\n")




