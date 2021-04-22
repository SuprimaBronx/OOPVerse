from containers import Container

def main():
    container = Container()
    input_name = str(input())
    output_name = str(input())
    file = open(input_name)
    container.in_data(file)
    file.close()
    file = open(output_name, "w")
    container.out(file)
    container.clear()
    container.out(file)
    file.close()

if __name__ == '__main__':
    main()