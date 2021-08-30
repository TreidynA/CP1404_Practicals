import random

MINIMUM = 1
MAXIMUM = 45
NUMBER_PER_LINE = 6

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    list_of_quick_picks = []
    for x in  range(NUMBER_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in list_of_quick_picks:
            number = random.randint(MINIMUM, MAXIMUM)
        list_of_quick_picks.append(number)
    list_of_quick_picks.sort()
    print(" ".join(f"{number:2}" for number in list_of_quick_picks))
