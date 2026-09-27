
"""
Module 2 — Lesson 4: Functions
Student: Alexander Viernes
Date: 2026-09-27

==================================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
==================================================

Functions are reusable blocks of code that perform
a specific task. Instead of writing the same code
multiple times, I can put that code inside a
function and run it whenever I need it.

==================================================
KEY VOCABULARY
==================================================

- function:  Named block of reusable code
- def: Python keyword used to create a function
- parameter: Variable listed in a function definition
- argument:  Value passed into a function when it is called
- return:  Keyword that sends a value back from a function
- function call: Running or using a function
- reusable code: Code that can be used many times without rewriting it

==================================================
MY OWN EXAMPLE(S)
==================================================
Write at least one working example below that you
came up with yourself  —  not copied from class.

"""

def calculate_batting_average(hits, at_bats):
    return hits / at_bats

player_hits = 42
player_at_bats = 120

average = calculate_batting_average(player_hits, player_at_bats)

print("Hits:", player_hits)
print("At Bats:", player_at_bats)
print("Batting Average:", round(average, 3))


"""

==================================================
A MISTAKE I MADE (or one I want to avoid)
==================================================

One mistake I made was confusing print() with
return. I thought printing a value automatically
sent it back from the function.

==================================================
HOW THIS CONNECTS TO SOMETHING ELSE
==================================================
[optional]
"""

