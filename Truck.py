from Car import Cars


class Trucks(Cars):

    def __init__(self):
        super().__init__()
        self.type = 'Truck'
        self.weight = 0

    def In(self, line):
        self.weight = line[1]
        self.engine_power = line[2]

    def display(self, file, i):
        file.write(str(i) + '.Грузовик' + "\n")
        file.write('грузоподъёмность: ' + str(self.weight) + "\n")

    def type_check(self):
        return self.type
