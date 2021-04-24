from class_define import in_data


class Container:

    def __init__(self):
        self.cars = []

    def in_data(self, file_input):
        for line in file_input:
            line = line.rstrip('\n')
            temp = line.split('|')
            for i in range(len(temp)):
                temp[i] = int(temp[i])
            cd = in_data(temp)
            self.cars.append(cd)


    def out(self, file):
        file.write('Контейнер содержит ' + str(len(self.cars))+' элементов \n')
        for i in range(len(self.cars)):
            self.cars[i].display(file, i)
            file.write('мощность двигателя: ' + str(self.cars[i].engine_power) + "\n")
        print('всё')

    def out_filtr(self, file_name):
        file_name.write('Контейнер содержит ' + str(len(self.cars)) + ' элементов \n')
        for i in range(len(self.cars)):
            self.cars[i].display_filtr(file_name, i)
            file_name.write('мощность двигателя: ' + str(self.cars[i].engine_power) + "\n")

    def clear(self):
        self.cars.clear()

