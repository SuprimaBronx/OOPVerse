from Car import Cars

class Light_car(Cars):

    def __init__(self):
        super().__init__()
        self.type = 'light_car'
        self.max_speed = 0

    def In(self, line):
        self.max_speed = line[1]
        self.engine_power = line[2]

    def display(self, file, i):
        file.write(str(i) + '.Легковая машина' + "\n")
        file.write('Максимальная скорость: ' + str(self.max_speed) + "\n")