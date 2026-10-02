"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    # Control the main thing
    score = float(input("Enter score: "))
    print(f"User score {score} is {get_result(score)}")
    random_score=random.randint(0,100)
    if score ==100:
        print("You get a prize!")
    print(f"Random: {random_score} = {get_result(random_score)}")

def get_result(score: float):
    # determine what result you get
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()