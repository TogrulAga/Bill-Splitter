# read test_file.txt
with open("test_file.txt", "r", encoding="utf-16") as file:
    print(file.readlines()[0])
