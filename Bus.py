from Car import Cars


class Buses(Cars):

    def __init__(self):
        super().__init__()
        self.type = 'Bus'
        self.passenger = 0

    def In(self, line):
        self.passenger = line[1]
        self.engine_power = line[2]

    def display(self, file, i):
        file.write(str(i) +'.Автобус' + "\n")
        file.write('пассажировместимость: ' + str( self.passenger) + "\n")


