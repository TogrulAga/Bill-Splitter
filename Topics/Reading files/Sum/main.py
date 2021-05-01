# read sums.txt
with open("sums.txt", "r") as file:
    for line in file.readlines():
        print(sum(int(line.rstrip("\n").split()[i]) for i in range(2)))
