from containers import Container

def main():
    x = 0
    container = Container()
    input_name = str(input())
    output_name = str(input())
    output_filtr_name = str(input())
    try:
        file = open(input_name)
    except:
        x = 4
    if x!=4:
        x = container.check(file)
        file.close()
    if x == 'x':
        file = open(input_name)
        container.in_data(file)
        file.close()
        container.sort()
        file = open(output_name, "w")
        file1 = open(output_filtr_name, "w")
        container.out(file,x)
        container.out_filtr(file1,x)
        container.clear()
        container.out(file,x)
        container.out_filtr(file1,x)
        file.close()
        file1.close()
    else:
        file = open(output_name, "w")
        file1 = open(output_filtr_name, "w")
        container.out(file, x)
        container.out_filtr(file1, x)
        file.close()
        file1.close()

if __name__ == '__main__':
    main()