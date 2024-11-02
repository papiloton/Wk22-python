with open("python.txt", 'w') as f:

    f.write("this is the first line\n")
    f.write("this is the second line\n")

    with open("python.txt", 'r') as f1:
        print(f1.readlines())