"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print(result_to_be_printed(score))
    print(result_to_be_printed(random.randint(0, 100)))


def result_to_be_printed(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score < 50:
            return "Bad"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"


main()