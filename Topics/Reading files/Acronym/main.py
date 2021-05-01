# read test.txt
with open("test.txt", "r") as file:
    for line in file.readlines():
        print(line[0])
