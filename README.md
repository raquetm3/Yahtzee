# Yahtzee

The game "yahtzee" is a game where you roll 5 dice, and various combinations of the dice are added to your scorecard. There are multiple categories for the scorecard, such as three of a kind, full house, large straight, yahtzee, etc. 

The purpose of the game is to get the highest score possible. 

This is normally a game where you play against at least one other player, and the player with the highest score is the winner. For now, I am just making a single player version. 

On a player's turn, there are three rounds of play. In the first round, the player rolls all five dice. After that, they have the option to fill in one of the boxes on their scorecard with the appropriate score, or roll the dice again. However, the player chooses the dice they want to reroll. The player can "save" some of the values of the dice that they roll. 

For example, if a player is trying to fill their scorecard for "four of a kind", and on their first dice roll, they roll a 3, three 4's, and a 6, the best move for the player would be to save the three 4's, and reroll the 3 and the 6. 

Whatever dice the player rolls on their third round must be added to the scorecard. If the dice rolled doesn't apply to a box on the scorecard and the player chooses to fill that box, they would earn the score of zero. For instance, if the player is trying to get a Yahtzee, and they don't roll 5 of the same number after three turns, a "0" must be entered on the scorecard.

In my version of the game, the score of the player will get updated on a csv file automatically. The following are the categories for the scorecard:
Ones  -  A sum of all the ones rolled
Twos  - A sum of all the twos rolled
Threes  - A sum of all the threes rolled
Fours - A sum of all the fours rolled
Fives - A sum of all the fives rolled
Sixes - A sum of all the sixes rolled
Sum  (The sum of the previous 6 categories)
Bonus (If the sum is >= 63, a 35 point bonus is added)
Three of a Kind (i.e, three 4's, or three 2's)  - The score is the sum of all dice rolled
Four of a Kind (i.e, four ones, four fives)  - The score is the sum of all dice rolled 
Full House (three of a kind, and two of another kind)  -  25 ponts
Small straight (four numbers in a sequence, i.e., 2,3,4,5  or  1,2,3,4)  -  30 points 
Large straight (five numbers in a sequence, i.e., 1,2,3,4,5)  -  40 points 
Chance (A sum of all the dice rolled, no matter the combination)
Yahtzee (Five of a kind)  -  50 points

Once a category in the scorecard is filled, then it can't be changed. However, if a player gets multiple Yahtzees, a 100 point bonus is added to their yahtzee box. There are normally other rules in this scenario, but to keep things simple for me this time around, only the 100 point bonus will be applied. 

At the end of the game, the scores in each category of the scorebox will be summed up and shown to the player. 

I hope you enjoy the game! :)

Requirements:
Python
Figlet Module (for title and end game screen) 
