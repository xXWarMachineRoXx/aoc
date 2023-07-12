## Problem Statement
### Day 1: Rock Paper Scissors 

--- Day 1: Calorie Counting ---
Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

```properties
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```
This list represents the Calories of the food carried by five Elves:

- The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
- The second Elf is carrying one food item with 4000 Calories.
- The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
- The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
- The fifth Elf is carrying one food item with 10000 Calories.
- In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

*Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?*

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