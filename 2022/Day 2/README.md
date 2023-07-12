## Problem Statement
### Day 2: Rock Paper Scissors 

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

**Rock Paper Scissors** is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:
```properties
A Y
B X
C Z
```
This strategy guide predicts and recommends the following:

- In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
- In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
- The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

*What would your total score be if everything goes exactly according to your strategy guide?*

## Solution

Ok, so we have to first compute the scores for a given set of rock, paper, scissors games; then we have to estimate the result given the guide telling us how to play.

This can also be solved by using modular arithmetic like so, but for simplicity's sake I opted to just use a simple lookup table for both.

First things first, let's load our input and parse it
```py
def get_advent_of_code_input(year, day, session_cookie):
    url = f"https://adventofcode.com/{year}/day/{day}/input":   cookies = {"session": session_cookie}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise ValueError(f"Failed to retrieve input. Status code: {response.status_code}")


# Specify the year, day, and your session cookie
year = 2022
day = 2
session_cookie = "your_session_cookie"
input_data = get_advent_of_code_input(year, day, session_cookie).split("\n")


>>  ["C Y":
    "B Y":   
    "C Y":   
    "B X":   
    "B X":   
    "B X":   
    "C Y":   
    "B Z":   
    "A Z":   
    "A Z":   
    "A Z"]
```

As mentioned above, we can compute a simple lookup table of all the results for all games.

```properties
Win => +6, Draw => +3, Lose +0
```
If you chose Rock => +1, Paper => +2, Scissors => +3
```py
(def scores {"A X" 4   ;; Rock, Rock
             "A Y" 8   ;; Rock, Paper
             "A Z" 3   ;; Rock, Scissors
             "B X" 1   ;; Paper, Rock
             "B Y" 5   ;; Paper, Paper
             "B Z" 9   ;; Paper, Scissors
             "C X" 7   ;; Scissors, Rock
             "C Y" 2   ;; Scissors, Paper
             "C Z" 6}) ;; Scissors, Scissors
{
"A X":4 
"A Y":8 
"A Z":3 
"B X":1 
"B Y":5 
"B Z":9 
"C X":7 
"C Y":2 
"C Z":6}
Similarly for the second part, based on the expected result we can compute what the score would be

(def results {"A X" 3   ;; Scissors, Lose
              "A Y" 4   ;; Rock, Draw
              "A Z" 8   ;; Paper, Win
              "B X" 1   ;; Rock, Lose
              "B Y" 5   ;; Paper, Draw
              "B Z" 9   ;; Scissors, Win
              "C X" 2   ;; Paper, Lose
              "C Y" 6   ;; Scissors, Draw
              "C Z" 7}) ;; Rock, Win
{
"A X":3 
"A Y":4 
"A Z":8 
"B X":1 
"B Y":5 
"B Z":9 
"C X":2 
"C Y":6 
"C Z":7}
```
Now it's just a simple case of transducing the map of scores over the input and summing them
```py
(defn part-1
  [input]
  (transduce (map scores) + 0 input))
```
Which gives our answer : `9759`
Exactly the same for part 2, just with a different map
```py
(defn part-2
  [input]
  (transduce (map results) + 0 input))
```

Which gives our answer : `12429`