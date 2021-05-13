from containers import Container

def main():
    container = Container()
    input_name = str(input())
    output_name = str(input())
    output_filtr_name = str(input())
    file = open(input_name)
    container.in_data(file)
    file.close()
    container.sort()
    file = open(output_name, "w")
    file1 = open(output_filtr_name, "w")
    container.out(file)
    container.out_filtr(file1)
    container.clear()
    container.out(file)
    container.out_filtr(file1)
    file.close()

if __name__ == '__main__':
    main()