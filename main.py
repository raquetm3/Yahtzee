from pyfiglet import Figlet
from random import randint
import re
import csv

# Yahtzee rules: You roll 5 dice trying to score points. each time you roll, you either score one category, or choose to roll some dice again.
# Three total chances to roll. You can only enter a score for each category once

# 13 rounds in total


class Die:
    def __init__(self, number, value):
        self.value = value
        self.number = number

    def value(self):
        return self.value

    def number(self):
        return self.number

    def roll(self):
        number = randint(1, 6)
        return number

    def __str__(self):
        return f"Die Number {self.number}: {self.value}"

    def __repr__(self):
        return f"Die Number {self.number}: {self.value}"


scorecard = [
    {"Category": "Ones", "Score": 0},
    {"Category": "Twos", "Score": 0},
    {"Category": "Threes", "Score": 0},
    {"Category": "Fours", "Score": 0},
    {"Category": "Fives", "Score": 0},
    {"Category": "Sixes", "Score": 0},
    {"Category": "Sum", "Score": 0},
    {"Category": "Bonus", "Score": 0},
    {"Category": "Three of a Kind", "Score": 0},
    {"Category": "Four of a Kind", "Score": 0},
    {"Category": "Full House", "Score": 0},
    {"Category": "Small Straight", "Score": 0},
    {"Category": "Large Straight", "Score": 0},
    {"Category": "Chance", "Score": 0},
    {"Category": "Yahtzee", "Score": 0}
]


#TODO figure out how to save dice, and unsave them, and update score


def main():
    dice = []
    for _ in range(1, 6):
        die = Die(number=str(_), value=None)
        dice.append(die)
    start()
    update_score(scorecard)
    saved_dice = []
    
    for _ in range(13):
        while True:
            scored = False
            # Roll 5 dice
            for _ in range(1,4):
                if scored == False
                    dice = dice_roll(dice)
                    print(f"\nRoll Number {_}\n")
                    print(*dice, sep="\n")

                    while True:
                        choice = input("What do you want to do next?  (save, unsave, score, or roll) ").lower().strip()
                        if choice == 'save':
                            to_be_saved = dice_input()
                            saved_dice.extend(to_be_saved)

                        #TODO add saved dice to new list and remove from dice list


                        elif choice == 'score':
                            score_dice()


                        elif choice == 'unsave':  #TODO remove from saved list and add to dice list
                            ...
                        elif choice == 'roll':
                            ...
                        else:
                            print("Invalid Input! You must input 'save', 'unsave', 'score', or 'roll'")

                else: #scored = true
                    break





def start():
    title = Figlet(font="larry3d")
    print(title.renderText("Yahtzee"))
    while True:
        ready = input("Are you ready to start the game? (y/n) ").strip().lower()
        if ready == "y":
            break
        elif ready == "n":
            print("Take your time")
        else:
            print("Invalid input!   (you must enter 'y' or 'n')")


def dice_roll(dice):
    for die in dice:
        die.value = randint(1, 6)
    return dice


def update_score(scorecard):
    with open("scorecard.tsv", "w", encoding="utf-8") as tsvfile:
        tsv_writer = csv.DictWriter(tsvfile, fieldnames=["Category", "Score"],delimiter='\t')
        tsv_writer.writeheader()
        tsv_writer.writerows(scorecard)

def dice_input():
    while True:
        die_numbers = input("Enter the number of the dice you would like to save, seperated by a space  (1,2,3,4, or 5): ").strip()
        pattern = r"^[1-5](?: [1-5]){0,4}$"
        match = re.search(pattern=pattern, string=die_numbers)
        if match:
            numbers = re.findall(r"[1-5]", die_numbers)
            if len(numbers) == len(set(numbers)):
                return numbers
            else:
                print("Invalid Input! There can't be duplicate dice!")
        else:
            print("Invalid Input! You must enter at most 5 numbers (1-5), and numbers must be seperated by a space!")


def score_dice()

if __name__ == "__main__":
    main()
