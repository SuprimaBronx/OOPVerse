from containers import Container

def main():
    container = Container()
    file = open('input_file.txt')
    container.in_data(file)
    file.close()
    file = open('output_file.txt', "w")
    container.out(file)
    container.clear()
    container.out(file)
    file.close()

if __name__ == '__main__':
    main()