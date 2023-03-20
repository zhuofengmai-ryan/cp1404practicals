"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

LOWEST_SCORE = 0
HIGHEST_SCORE = 100
score = float(input("Enter score: "))
if score < LOWEST_SCORE or score > HIGHEST_SCORE:
    print("Invalid score")
else:
    if score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    elif score < 50:
        print("Bad")
