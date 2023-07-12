import requests
from itertools import product

def get_advent_of_code_input(year, day, session_cookie):
    url = f"https://adventofcode.com/2022/day/2/input"
    cookies = {"session": session_cookie}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise ValueError(f"Failed to retrieve input. Status code: {response.status_code}")


# Specify the year, day, and your session cookie
year = 2022
day = 2
session_cookie = "53616c7465645f5f1d4febfbd32b1e83d3a73f9839146862cf24e6fa726d772e84d5e47e79b23c8641d7fb5f1e414dacb340bcb0f00d950d2c674025a6b6b6bf"

# Call the function to get the Advent of Code input
input_data = get_advent_of_code_input(year, day, session_cookie).split("\n")

# Map the input to points
win_points_part_2={"A X":3,"A Y":4,"A Z":8,"B X":1,"B Y":5,"B Z":9,"C X":2,"C Y":6,"C Z":7}

points=0
for i in input_data:
    if i in win_points_part_2:
        points+=win_points_part_2[i]

# Print Total points for part 2
print(points)