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

    def multimethods(self, file_name):
        try:
            for i in range(0, len(self.cars), 2):
                file_name.write(self.cars[i].type_check() + ' and ' + self.cars[i + 1].type_check() + '\n')
        except:
            file_name.write(self.cars[-1].type_check()+ ' alone' + '\n')

    def clear(self):
        self.cars.clear()

