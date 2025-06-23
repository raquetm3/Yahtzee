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


# TODO figure out how to update score
# TODO Can't save/unsave dice that are already saved/unsaved
# TODO Test end game function


def main():
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
        {"Category": "Yahtzee", "Score": 0},
    ]
    unscored = [
        "Ones",
        "Twos",
        "Threes",
        "Fours",
        "Fives",
        "Sixes",
        "Three of a Kind",
        "Four of a Kind",
        "Full House",
        "Small Straight",
        "Large Straight",
        "Chance",
        "Yahtzee",
    ]
    initial_dice = []
    for _ in range(1, 6):
        die = Die(number=str(_), value=None)
        initial_dice.append(die)
    start()
    update_score(scorecard)

    for _ in range(1, 14):  # 13 rounds of play
        print(f"Round Number {_}\n")
        while True:
            scored = False
            saved_dice = []
            dice = initial_dice.copy()
            # Roll 5 dice
            for x in range(1, 4):  # at most three rolls per round
                if scored == False:
                    dice = dice_roll(dice)
                    print(f"Saved Dice: {saved_dice}\n")
                    print(f"Roll Number {x}\n")
                    print(*dice, sep="\n")

                    while True:
                        if x < 3:
                            choice = (
                                input(
                                    "\nWhat do you want to do next?  (save, unsave, score, or roll) "
                                )
                                .lower()
                                .strip()
                            )
                            if choice == "save":
                                if len(saved_dice) == 5:
                                    print("All dice are already saved!")

                                else:
                                    to_be_saved = dice_input(save="save")
                                    for number in to_be_saved:
                                        for die in dice:
                                            if number == die.number:
                                                saved_dice.append(die)
                                                dice.remove(die)
                                    print(f"\nSaved Dice: {saved_dice}")
                                    print(f"\nUnsaved Dice: {dice}")

                            elif choice == "score":
                                scorecard = score_dice(
                                    saved_dice, dice, scorecard, unscored
                                )
                                scored = True
                                update_score(scorecard)
                                break

                            elif choice == "unsave":
                                if len(dice) == 5:
                                    print("All dice are already unsaved!")
                                else:
                                    to_be_unsaved = dice_input(save="unsave")
                                    for number in to_be_unsaved:
                                        for die in saved_dice:
                                            if number == die.number:
                                                saved_dice.remove(die)
                                                dice.append(die)
                                    print(f"\nSaved Dice: {saved_dice}")
                                    print(f"\nUnsaved Dice: {dice}")

                            elif choice == "roll":
                                if len(saved_dice) == 5:
                                    print(
                                        "\nYou can't roll because all dice are saved! Unsave some dice if you want to roll again"
                                    )
                                    print(f"\nSaved Dice: {saved_dice}")
                                    print(f"\nUnsaved Dice: {dice}")

                                else:
                                    break

                            else:
                                print(
                                    "\nInvalid Input! You must input 'save', 'unsave', 'score', or 'roll'"
                                )

                        else:  # x = 3
                            scorecard = score_dice(
                                saved_dice, dice, scorecard, unscored
                            )
                            update_score(scorecard)
                            scored = True
                            break

                else:  # scored = true
                    break

            break

    end(scorecard)

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
        tsv_writer = csv.DictWriter(
            tsvfile, fieldnames=["Category", "Score"], delimiter="\t"
        )
        tsv_writer.writeheader()
        tsv_writer.writerows(scorecard)


def dice_input(save):
    while True:
        if save == "save":
            die_numbers = input(
                "\nEnter the number of the dice you would like to save, seperated by a space  (1,2,3,4, or 5): "
            ).strip()

        else:  # save == "unsave"
            die_numbers = input(
                "\nEnter the number of the dice you would like to unsave, seperated by a space  (1,2,3,4, or 5): "
            ).strip()

        pattern = r"^[1-5](?: [1-5]){0,4}$"
        match = re.search(pattern=pattern, string=die_numbers)
        if match:
            numbers = re.findall(r"[1-5]", die_numbers)
            if len(numbers) == len(set(numbers)):
                return numbers
            else:
                print("Invalid Input! There can't be duplicate dice!")
        else:
            print(
                "Invalid Input! You must enter at most 5 numbers (1-5), and numbers must be seperated by a space!"
            )


def score_dice(saved_dice, dice, scorecard, unscored):
    print("\nHere are the dice that will be scored:\n")
    dice.extend(saved_dice)
    dice.sort(key=lambda x: x.number)
    print(*dice, sep="\n")
    print("\nWhat category would you like to score with these dice?\n")
    x = 1
    for category in unscored:
        print(f"{x} - {category}")
        x += 1

    category = score_category_check(unscored)



def score_category_check(unscored):
    while True:
        try:
            category = int(input(
                "\nEnter the number associated with the category you would like to score: "
            ))

            if category > len(unscored):
                raise ValueError

            elif category <= 0:
                raise ValueError

        except ValueError:
            print("Invalid input, you must enter a number associated with one of the available categories!")

        else:
            return category


def end(scorecard):
    title = Figlet(font="standard")
    print(title.renderText("Game Over!"))
    final_score = 0
    for category in scorecard:
        final_score += scorecard["Score"]

    print(f"Congratulations on a great game of Yahtzee! Your final score is {final_score}!" )

if __name__ == "__main__":
    main()
