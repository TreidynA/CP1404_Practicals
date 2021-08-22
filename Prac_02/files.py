name = input("Name: ")
OUTPUT_FILE = open("name.txt", "w")
print(name, end="", file=OUTPUT_FILE)
OUTPUT_FILE.close()

INPUT_FILE = open("name.txt", "r")
print(f"Your name is {INPUT_FILE.readline()}")
INPUT_FILE.close()

INPUT_FILE = open("numbers.txt", "r")
number_1 = INPUT_FILE.readline()
number_2 = INPUT_FILE.readline()
print(int(number_1) + int(number_2))
INPUT_FILE.close()

INPUT_FILE = open("numbers.txt", "r")
total = 0
for line in INPUT_FILE:
    total += int(line)
print(total)
INPUT_FILE.close()