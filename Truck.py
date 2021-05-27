from Car import Cars


class Trucks(Cars):

    def __init__(self):
        super().__init__()
        self.type = 'Truck'
        self.weight = 0

    def in_information(self, line):
        self.weight = line[1]
        self.engine_power = line[2]
        self.fuel_consumption = line[3]
        self.global_weight = line[1]
        self.ratio_calc()

    def display(self, file, i):
        file.write(str(i) + '.Грузовик' + "\n")
        file.write('грузоподъёмность: ' + str(self.weight) + "\n")

    def display_filtr(self, file, i):
        file.write(str(i) + '.Грузовик' + "\n")
        file.write('грузоподъёмность: ' + str(self.weight) + "\n")
        file.write('мощность двигателя: ' + str(self.engine_power) + "\n")
        file.write('расход топлива: ' + str(self.fuel_consumption) + "\n")
        file.write('отношение веса груза к мощности двигателя: ' + str(self.ratio) + "\n")
